import os

import sys

import django

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django): django.setup()

from info.models import CourseInfo

def search_test():
    #c = CourseInfo()
    print("hello world")
    kw = input("keyword: ")
    kw = kw.upper()
    dept_kw = input("department: ")
    sort_option = input("choose sort option (title, courseid): ")
    dept_kw = dept_kw.upper()
    global result
    #search in all departments
    if dept_kw == "ALL":
        print("searching in all depts")
        result1 = CourseInfo.objects.filter(course_code__iexact=kw).order_by('title')
        result2 = CourseInfo.objects.filter(title__icontains=kw).order_by('title')
        result3 = CourseInfo.objects.filter(description__icontains=kw).order_by('title')
        result = result1 | result2 | result3
        result.distinct()
    else:
        result1 = CourseInfo.objects.filter(dept=dept_kw).filter(course_code__iexact=kw).order_by('title')
        result2 = CourseInfo.objects.filter(dept=dept_kw).filter(title__icontains=kw).order_by('title')
        result3 = CourseInfo.objects.filter(dept=dept_kw).filter(description__icontains=kw).order_by('title')
        result = result1 | result2 | result3
        result.distinct()
    if sort_option == "title":
        result = result.order_by('title')
    elif sort_option == "courseid":
        result = result.order_by('course_code')
    for x in range(0, len(result)):
        print(result[x].title)
    return result


if __name__ == '__main__':
   search_test()




