from django.conf.urls import url
from django.contrib import admin

from controller import views as controller_views

urlpatterns = [
    # Home page.
    url(r'^$', controller_views.HomeView.as_view(), name = "home"),
    # The aboutme page
    url(r'^about/$', controller_views.AboutView.as_view(),
        name = "about"),
    url(r'^resume/$', controller_views.resume_view, name = 'resume'),
    url(r'^blog/$', controller_views.BlogView.as_view(), name = 'blog'),
    url(r'^projects/$', controller_views.ProjectsView.as_view(), name = 'projects'),
    url(r'^other/$', controller_views.OtherView.as_view(), name = 'other'),
    url(r'^admin/', admin.site.urls),
]
