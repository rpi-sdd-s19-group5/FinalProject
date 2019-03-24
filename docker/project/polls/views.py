from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from info.search_test import search_test
from info.search_test import search_test_prof
from django.template import loader
from info.models import CourseInfo, ProfInfo

from info.models import CourseInfo


def index(request):
    return render(request, 'polls/main.html')


def index_prof(request):
    return render(request, 'polls/main_faculty.html')


def search_course(request):
    if request.GET:
        print(request.GET)
        dept = request.GET["dept"].split(":")[1]
        dept = ("ALL" if dept == "All Departments" else dept)
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


def course_detail(request, name_num):
    course = CourseInfo.objects.filter(course_code=name_num)
    if len(course) == 1:
        return render(request, 'polls/search_course.html')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search_prof(request):
    if request.GET:
        print(request.GET)
        search_content = request.GET["search_content"]
        print(search_content)
        prof_result = ProfInfo.search_test_prof(search_content)[:10]
        for prof in prof_result: prof["dept"] = prof["dept"].replace('|', ' ')
        context = {
            'search_results': prof_result,
            'search_content': search_content,
        }
    else:
        prof_result = ProfInfo.objects.all()[:10]
        for prof in prof_result: prof.dept = prof.dept.replace('|', ' ')
        context = {
            'search_results': prof_result,
        }

    return render(request, 'polls/search_faculty.html', context)


def prof_detail(request):
    return None
