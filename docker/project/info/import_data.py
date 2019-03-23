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
        title = course["title"]
        dept = course["title"][0:4].upper()
        course_code = course["title"].split('-', 1)[0].strip()
        description = course["description"]
        prerequisites = (None if not course["prerequisites"] else course["prerequisites"].split(" ", 1)[1])
        offered = (None if not course["offered"] else course["offered"])
        cross_listed = (None if not course["cross_listed"] else course["cross_listed"])
        credit_hours = (None if not course["credit_hours"] else int(re.findall("\d+", course["credit_hours"])[0]))
        c, created = CourseInfo.objects.update_or_create(
            title=title, dept=dept, course_code=course_code, description=description, prerequisites=prerequisites,
            offered=offered, cross_listed=cross_listed, credit_hours=credit_hours
        )
