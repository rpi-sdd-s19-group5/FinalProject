import os
import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()

from info.models import ProfAndCourses
import json


def json_to_dict():
    results = []
    with open("info/19Spring.json") as json_file:
        data = json.load(json_file)
        for x in range(9, len(data) - 1):
            # print(data[x])
            if len(data[x]) == 0:
                continue
            else:
                entry = {}
                entry["dept"] = data[x]["Subj"].strip()
                entry["code_digit"] = data[x]["Crse"].strip()
                entry["course_code"] = entry["dept"] + " " + entry["code_digit"]
                entry["section"] = data[x]["Sec"].strip()
                entry["credit"] = data[x]["Cred"].strip()

                # Check whether course has multiple sections
                if not entry["dept"]:
                    last = ProfAndCourses.objects.latest()
                    entry["dept"] = last.dept
                    entry["code_digit"] = last.code_digit
                    entry["course_code"] = last.course_code
                    entry["section"] = last.section
                    entry["credit"] = last.credit

                entry["prof"] = ' '.join(data[x]["Instructor"].split())
                entry["days"] = data[x]["Days"]
                entry["time"] = data[x]["Time"]
                entry["date"] = data[x]["Date"]
                entry["location"] = data[x]["Location"]

                # Update in database item
                ProfAndCourses.objects.bulk_create(results)
                ProfAndCourses.objects.update_or_create(
                    course_code=entry["course_code"], dept=entry["dept"], prof=entry["prof"],
                    code_digit=entry["code_digit"],
                    credit=entry["credit"],
                    date=entry["date"], days=entry["days"], time=entry["time"], location=entry["location"],
                    section=entry["section"]
                )

    for entry in results:
        ProfAndCourses().objects.update_or_create(
            course_code=entry["course_code"], dept=entry["dept"], prof=entry["prof"], code_digit=entry["code_digit"],
            credit=entry["credit"],
            date=entry["date"], days=entry["days"], time=entry["time"], location=entry["location"],
            section=entry["section"]
        )


if __name__ == '__main__':
    json_to_dict()
