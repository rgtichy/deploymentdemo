from django.conf.urls import url, include
from django.contrib import admin
from . import views
# import re

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create$',views.create, name='create'),
    url(r'^(?P<id>\d+)/edit$',views.update, name='edit'),
    url(r'^(?P<id>\d+)/delete$',views.delete, name='delete'),
    url(r'^(?P<id>\d+)$',views.showCourse, name='show'),
]
