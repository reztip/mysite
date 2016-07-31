from django.conf.urls import url
from django.contrib import admin

from controller import views as controller_views

urlpatterns = [
    url(r'^about/', controller_views.AboutView.as_view()),
    url(r'^admin/', admin.site.urls),
]
