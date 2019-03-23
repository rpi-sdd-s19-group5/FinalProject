import os
import re
import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()

from info.models import CourseInfo
from info.models import ProfAndCourses
import json
from typing import Dict


def json_to_dict():
    results = []
    with open("info/19Spring.json") as json_file:
        data = json.load(json_file)
        for x in range(9, len(data) - 1):
            print(data[x])
            if len(data[x]) == 0:
                continue
            else:
                entry: Dict[str, str] = {"course_code": "", "dept": "", "code_digit": "", "prof": "",
                                         "section": "", "credit": "", "days": "", "time": "", "date": "",
                                         "location": ""}
                entry["dept"] = data[x]["Subj"]
                entry["code_digit"] = data[x]["Crse"]
                entry["course_code"] = entry["dept"] + " " + entry["code_digit"]
                entry["prof"] = ' '.join(data[x]["Instructor"].split())
                entry["section"] = data[x]["Sec"]
                entry["credit"] = data[x]["Cred"]
                entry["days"] = data[x]["Days"]
                entry["time"] = data[x]["Time"]
                entry["data"] = data[x]["Date"]
                entry["location"] = data[x]["Location"]
                results.append(entry)
    for entry in results:
        temp = ProfAndCourses()
        temp.course_code = entry["course_code"]
        temp.dept = entry["dept"]
        temp.code_digit = entry["code_digit"]
        temp.credit = entry["credit"]
        temp.date = entry["date"]
        temp.days = entry["days"]
        temp.time = entry["time"]
        temp.location = entry["location"]
        temp.section = entry["section"]
        temp.save()


if __name__ == '__main__':
    json_to_dict()
