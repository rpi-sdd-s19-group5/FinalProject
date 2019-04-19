import os
import sys

import django
from info.models import ProfAndCourses
import json

# environment setup
sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django):
    django.setup()


# convert json to dict format
def json_to_dict():
    results = []
    # opens the json file
    with open("19Spring.json") as json_file:
        # load stuff
        data = json.load(json_file)
        # skipping the first 9 rows because of the data structure
        for x in range(9, len(data) - 1):
            # print(data[x])
            # if it's an empty row
            if len(data[x]) == 0:
                continue
            # otherwise we'll start reading stuff
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
                # update the dict
                entry["prof"] = ' '.join(data[x]["Instructor"].split())
                print(entry["prof"])
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
    # update faculty & course relation in database
    for entry in results:
        # insert stuff into the database
        ProfAndCourses().objects.update_or_create(
            course_code=entry["course_code"], dept=entry["dept"], prof=entry["prof"], code_digit=entry["code_digit"],
            credit=entry["credit"],
            date=entry["date"], days=entry["days"], time=entry["time"], location=entry["location"],
            section=entry["section"]
        )
    return


if __name__ == '__main__':
    json_to_dict()
