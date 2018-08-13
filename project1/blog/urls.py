from django.contrib import admin
from django.urls import path,re_path

from .views import blog_list,blog_detail
urlpatterns = [
	path('',blog_list,name='blog_list'),
	re_path(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', blog_detail,name='blog_detail'),
]
