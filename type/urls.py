from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^types$', views.index,name="types"),
    url(r'^types/create/$', views.create,name="types_create"),
    url(r'^types/(?P<id>\d+)/delete/$', views.delete,name="types_delete"),
    url(r'^types/(?P<id>\d+)/edit/$', views.edit, name="types_edit"),
]