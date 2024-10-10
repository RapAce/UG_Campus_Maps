from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^events$', views.index,name="events"),
    url(r'^event/create/$', views.create,name="events_create"),
    url(r'^event/(?P<id>\d+)/delete/$', views.delete,name="events_delete"),
    url(r'^event/(?P<id>\d+)/edit/$', views.edit, name="events_edit"),
]