from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([a-zA-Z]+)$', views.index),
    url(r'^', views.index, name='ninjas'),
]
