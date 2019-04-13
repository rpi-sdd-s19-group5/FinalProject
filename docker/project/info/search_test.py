import os

import sys

import django
from info.models import ProfInfo
from info.models import CourseInfo

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()


def search_course_tool(kw, dept_kw, sort_option=1):
    kw = kw.upper()
    dept_kw = dept_kw.upper()
    global result
    # search in all departments
    if dept_kw == "ALL":
        print(sort_option)
        print("searching in all depts")
        result1 = CourseInfo.objects.filter(course_code__iexact=kw)
        result2 = CourseInfo.objects.filter(title__icontains=kw)
        result3 = CourseInfo.objects.filter(description__icontains=kw)
        result = result1 | result2 | result3
        result.distinct()
    else:
        result1 = CourseInfo.objects.filter(dept=dept_kw).filter(course_code__iexact=kw)
        result2 = CourseInfo.objects.filter(dept=dept_kw).filter(title__icontains=kw)
        result3 = CourseInfo.objects.filter(dept=dept_kw).filter(description__icontains=kw)
        result = result1 | result2 | result3
        result.distinct()
    if sort_option == "1":
        print("order1")
        result = result.order_by('title')
    elif sort_option == "2":
        print("order")
        result = result.order_by('course_code')
    # for x in range(0, len(result)):
    #     print(result[x].title)
    result_2 = list(result.values())
    # print(result_2)
    return result_2


def search_prof(kw):
    kw = kw.upper()
    result_1 = ProfInfo.objects.filter(name__icontains=kw).order_by('name')
    result_2 = list(result_1.values())
    return result_2


if __name__ == '__main__':
    search_course_tool("materials", "arch")
