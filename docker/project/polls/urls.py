from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name="test"),
    path('test2', views.test2, name="test2"),
    path('test4',views.test4,name="test4")
]
