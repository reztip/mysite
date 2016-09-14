from django.conf.urls import url, include
from django.contrib import admin

from . import views 
urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^login/$', views.login, name = 'login'),
        url(r'^logout/$', views.logout, name = 'logout'),
        url(r'^new_user$', views.new_user, name = 'new_user'),
        ]
