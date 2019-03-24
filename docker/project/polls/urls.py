from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_course', views.course, name="search_course")
]
