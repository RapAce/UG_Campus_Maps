from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^categories$', views.index,name="categories"),
    url(r'^categories/create/$', views.create,name="categories_create"),
    url(r'^categories/(?P<id>\d+)/delete/$', views.delete,name="categories_delete"),
    url(r'^categories/(?P<id>\d+)/edit/$', views.edit, name="categories_edit"),
]