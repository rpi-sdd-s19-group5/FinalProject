import os
import re
import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()

from info.models import CourseInfo
from info.course_info import course_info_crawler

if __name__ == '__main__':
    course_info = course_info_crawler()
    for course in course_info:
        print(course)
        c = CourseInfo()
        c.title = course["title"]
        c.description = course["description"]
        if not course["prerequisites"]:
            c.credit_hours = None
        else:
            c.prerequisites = course["prerequisites"].split(" ", 1)[1]
        c.offered = course["offered"]
        c.cross_listed = course["cross_listed"]
        if not course["credit_hours"]:
            c.credit_hours = None
        else:
            c.credit_hours = int(re.findall("\d+", course["credit_hours"])[0])
        print(c)
        c.save()
