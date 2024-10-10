from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(?P<id>\d+)/details/$', views.details,name="index_details"),

    url(r'^exams$', views.examindex,name="exam_index"),
    url(r'^exams/(?P<id>\d+)/details/$', views.examdetails,name="exam_details"),
]