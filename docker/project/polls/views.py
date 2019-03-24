from django.http import HttpResponse
from django.shortcuts import render
from info.search_test import search_test
from django.template import loader
from info.models import CourseInfo

def index(request):
    return render(request, 'polls/main.html')


def course(request):
    return render(request, 'polls/search_course.html')


def test(request):
    course_result = search_test("materials", "arch")
    template = loader.get_template('polls/search_course.html')
    course_result = course_result[0:10]
    for result in course_result:
        temp = result['description'].split()
        temp2 = ""
        for x in range(0, 40):
            temp2 += temp[x]
            temp2 += " "
        temp2.strip()
        temp2 += "..."
        result['description'] = temp2
    context = {
        'search_results' : course_result,

    }
    print(course_result)
    return render(request, 'polls/search_course.html', context)

course_result = search_test("materials", "arch")
course_result = course_result[0:10]
for result in course_result:
    temp = result['description'].split()
    temp2 = ""
    for x in range(0, 30):
        temp2 += temp[x]
        temp2 += " "
    temp2.strip()
    temp2 += "..."
    result['description'] = temp2
    print(temp2)