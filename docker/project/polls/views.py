from django.http import HttpResponse
from django.shortcuts import render

from info.search_test import search_test
from info.search_test import search_test_prof
from django.template import loader
from info.models import CourseInfo


def index(request):
    return render(request, 'polls/main.html')


def search_course(request):
    if request.GET:
        print(request.GET)
        dept = request.GET["dept"]
        search_content = request.GET["search_content"]
        print(dept)
        print(search_content)
        course_result = search_test(search_content, dept)[:10]
        context = {
            'search_results': course_result,
            'dept': dept,
            'search_content': search_content,
        }

    else:
        course_result = CourseInfo.objects.all()[:10]
        context = {
            'search_results': course_result,
        }

    print(course_result)
    return render(request, 'polls/search_course.html', context)


# def test(request):
#     course_result = search_test("materials", "arch")
#     course_result = course_result[0:10]
#     for result in course_result:
#         temp = result['description'].split()
#         temp2 = ""
#         for x in range(0, 40):
#             temp2 += temp[x]
#             temp2 += " "
#         temp2.strip()
#         temp2 += "..."
#         result['description'] = temp2
#     context = {
#         'search_results': course_result,
#     }
#     print(course_result)
#     return render(request, 'polls/search_course.html', context)


def test2(request):
    return render(request, 'polls/course.html')


def course_detail(request):
    return None


def search_prof(request):
    return None


def test_prof_result(request):
    prof_result = search_test_prof("Jeff")
    template = loader.get_template('polls/search_faculty.html')
    prof_result = prof_result[0:10]
    context = {
        'search_results': prof_result,
    }
    return render(request, 'polls/search_faculty.html', context)
