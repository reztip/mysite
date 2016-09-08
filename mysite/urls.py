from django.conf.urls import url, include
from django.contrib import admin

from controller import views as controller_views

urlpatterns = [
    # Home page.
    url(r'^$', controller_views.HomeView.as_view(), name = "home"),
    # The aboutme page
    url(r'^about(me)?/$', controller_views.AboutView.as_view(),
        name = "about"),
    url(r'^resume/$', controller_views.resume_view, name = 'resume'),
    url(r'^projects/$', controller_views.projects_view, name = 'projects'),
    url(r'^projects/(?P<name>[a-z]+)/$', controller_views.project_detail_view, name = 'project_detail'),
    url(r'^other/$', controller_views.OtherView.as_view(), name = 'other'),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs?/', include('blog.urls', namespace = 'blog')),
    url(r'^finances?/', include('finance.urls', namespace = 'finance')),
]
