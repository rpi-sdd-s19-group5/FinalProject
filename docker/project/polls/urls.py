from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_course', views.search_course, name="search_course"),
    path('course/<name_num>',views.course_detail, name="course_detail" ),

    path('test', views.test, name="test"),
    path('test2', views.test2, name="test2"),
]
