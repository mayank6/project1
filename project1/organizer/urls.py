from django.contrib import admin
from django.urls import path,re_path

from .views import tag_list,tag_detail,startup_list,startup_detail
urlpatterns = [
    path('', tag_list,name='home'),
     re_path(r'^tag/(?P<slug>[\w-]+)/$',tag_detail,name='tag_detail'),
     path('startup/',startup_list,name='startup_list'),
     re_path(r'^startup/(?P<slug>[\w-]+)/$',startup_detail,name='startup_detail'),
]
