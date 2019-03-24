import os

import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()
from info.models import ProfInfo
from info.models import CourseInfo
from info.models import ProfAndCourses

def search_test(kw):
    result = ProfAndCourses.objects.filter(prof__icontains=kw)
    result_2 = list(result.values("course_code"))
    #print(result_2)
    result_3 = []
    for x in result_2:
        if CourseInfo.objects.filter(course_code__icontains=x['course_code']).values():
            result_3.append(list(CourseInfo.objects.filter(course_code__icontains=x['course_code']).values())[0])
    #result_3 = list(result_3.values())
    for x in result_3:
        print(x['title'])
    return result_3

if __name__ == '__main__':
    search_test("lirong xia")