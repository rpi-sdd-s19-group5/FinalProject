from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'polls/main.html')


def course(request):
    return render(request, 'polls/search_course.html')
