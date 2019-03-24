from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_course', views.search_course, name="search_course"),
    path('test', views.test, name="test"),
    path('test_prof_result', views.test_prof_result, name="test_prof_result")
]
