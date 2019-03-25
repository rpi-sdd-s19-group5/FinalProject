import os
import re
import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()

from info.models import CourseInfo, ProfInfo


def update_course_info(course):
    title = course["title"].split("-")[1].strip()
    dept = course["title"][0:4].upper()
    course_code = course["title"].split('-', 1)[0].strip()
    description = course["description"]
    try:
        prerequisites = (None if not course["prerequisites"] else course["prerequisites"].split(" ", 1)[1])
    except IndexError as e:
        prerequisites = None
        print("Prerequisites/Corequisites Error, Maybe format error")

    offered = (None if not course["offered"] else course["offered"])
    cross_listed = (None if not course["cross_listed"] else course["cross_listed"])

    # Check the format of credit hours
    try:
        credit_hours = (None if not course["credit_hours"] else int(re.findall("\d+", course["credit_hours"])[0]))
    except IndexError as e:
        credit_hours = None
        print("Credit Hours Error, maybe no standard number")

    # Update or create data instance
    CourseInfo.objects.update_or_create(
        title=title, dept=dept, course_code=course_code, description=description, prerequisites=prerequisites,
        offered=offered, cross_listed=cross_listed, credit_hours=credit_hours
    )


def update_prof_info(prof):
    url = prof["url"]
    name = prof["name"][0]
    title = '|'.join(prof["title"])
    dept = '|'.join(prof["department"])
    email = '|'.join(prof["email"])
    web_page = '|'.join(prof["web_page"])
    focus = '|'.join(prof["focus"])
    education = '|'.join(prof["education"])
    biography = ' '.join(prof["biography"])
    image = ''.join(prof["image"])
    ProfInfo.objects.update_or_create(
        url=url, name=name, title=title, dept=dept, email=email, web_page=web_page, focus=focus, education=education,
        biography=biography, image=image
    )


# from info.models import CourseInfo
# from info.course_info import course_info_crawler
#
# if __name__ == '__main__':
#     course_info = course_info_crawler()
#     for course in course_info:
#         c = CourseInfo()
#         temp = course["title"].split()
#         temp2 = ""
#         for x in range(3, len(temp)):
#             if x != len(temp) - 1:
#                 temp2 += temp[x]
#                 temp2 += " "
#             else:
#                 temp2 += temp[x]
#         c.title = temp2
#         c.dept = course["title"][0:4].upper()
#         print(c.dept)
#
#
#         c.course_code = temp[0] + " " + temp[1]
#         print(c.course_code)
#         c.description = course["description"]
#         c.prerequisites = course["prerequisites"]
#         c.offered = course["offered"]
#         c.cross_listed = course["cross_listed"]
#         if not course["credit_hours"]:
#             c.credit_hours = None
#         else:
#             c.credit_hours = int(re.findall("\d+", course["credit_hours"])[0])
#         c.save()
#
