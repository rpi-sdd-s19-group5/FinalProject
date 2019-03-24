from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main.html', RedirectView.as_view(pattern_name='index')),

    path('prof', views.index_prof, name="index_prof"),
    path('main_faculty.html', RedirectView.as_view(pattern_name='index_prof')),

    # Course info
    path('search_course', views.search_course, name="search_course"),
    path('course/<name_num>', views.course_detail, name="course_detail"),

    # Prof info
    path('search_prof', views.search_prof, name="search_prof"),
    path('prof/<name_num>', views.prof_detail, name="search_prof"),

    # path('test', views.test, name="test"),
]
