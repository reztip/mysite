from django.conf.urls import url, include
from django.contrib import admin

from . import views as blog_views
urlpatterns = [
    url(r'^$', blog_views.index, name = 'index'),
    url(r'^(?P<pk>\d+)/$', blog_views.detail, name = 'detail'),
    ]
