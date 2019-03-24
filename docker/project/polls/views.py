from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from info.models import CourseInfo
from info.models import ProfInfo
from info.models import ProfAndCourses


def index(request):
    return render(request, 'polls/main.html')


def search_course(request):
    if request.GET:
        print(request.GET)
    return render(request, 'polls/search_course.html')


def test(request):
    return None


def test2(request):
    courseinfo = CourseInfo.objects.all()[1]
    context = {'courseinfo':courseinfo}
    return render(request, 'polls/course.html',context)

def test4(request):
    profinfo = ProfInfo.objects.all()[0]
    profcourse =ProfAndCourses.objects.all()
    context = {'profinfo':profinfo,'profcourse':profcourse}
    return render(request, 'polls/faculty.html',context)

