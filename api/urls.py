from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^api$', views.index,name="api"),
    url(r'^api/events/$', views.EventList,name="api_events"),
    url(r'^api/events/(?P<id>\d+)/$', views.Eventdetail,name="api_events_details"),
    url(r'^api/examevents/$', views.ExamEventList,name="api_examevents"),
    url(r'^api/examevents/(?P<id>\d+)/$', views.ExamEventdetail,name="api_examevents_details"),
]