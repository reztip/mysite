from django.conf.urls import url, include
from django.contrib import admin

from . import views as blog_views
urlpatterns = [
    url(r'^$', blog_views.index, name = 'index'),
    url(r'^(?P<pk>\d+)/$', blog_views.detail, name = 'detail'),
    url(r'^(?P<pk>\d+)/edit/$', blog_views.edit, name = 'edit'),
    url(r'^search/$', blog_views.search, name = 'search'),
    url(r'^new/$', blog_views.new_post, name = 'new_post'),
    ]
