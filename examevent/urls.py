from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^examevents$', views.index,name="examevents"),
    url(r'^examevent/create/$', views.create,name="examevents_create"),
    url(r'^examevent/(?P<id>\d+)/delete/$', views.delete,name="examevents_delete"),
    url(r'^examevent/(?P<id>\d+)/edit/$', views.edit, name="examevents_edit"),
]