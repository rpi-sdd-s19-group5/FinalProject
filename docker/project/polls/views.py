from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'polls/main.html')


def search_course(request):
    if request.GET:
        print(request.GET)
    return render(request, 'polls/search_course.html')


def test(request):
    return None


def test2(request):
    return render(request, 'polls/course.html')
