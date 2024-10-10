from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^login$', views.index,name="authenticate"),
    url(r'^logout$', views.out,name="logout"),
]