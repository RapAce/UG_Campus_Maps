from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^home$', views.index,name="home"),

]