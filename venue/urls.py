from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^venues$', views.index,name="venues"),
    url(r'^venues/create/$', views.create,name="venues_create"),
    url(r'^venues/(?P<id>\d+)/delete/$', views.delete,name="venues_delete"),
    url(r'^venues/(?P<id>\d+)/edit/$', views.edit, name="venues_edit"),

]