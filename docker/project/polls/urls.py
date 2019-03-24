from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Course info
    path('search_course', views.search_course, name="search_course"),
    path('course/<name_num>', views.course_detail, name="course_detail"),

    # Prof info
    path('search_prof', views.search_prof, name="search_prof"),
    path('prof/<name_num>', views.search_prof, name="search_prof"),

    # path('test', views.test, name="test"),
    path('test2', views.test2, name="test2"),
]
