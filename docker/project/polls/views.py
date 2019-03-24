from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from info.models import CourseInfo


def index(request):
    print("233")
    return render(request, 'polls/main.html')


def search_course(request):
    if request.GET:
        print(request.GET)
        dept = request.GET["dept"]
        search_content = request.GET["search_content"]
        return render(request, 'polls/search_course.html')
    else:
        data = CourseInfo.objects.all()[:5]
        return render(request, 'polls/search_course.html')


def test(request):
    return None


def test2(request):
    return render(request, 'polls/course.html')


def course_detail(request):
    return None