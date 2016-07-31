from django.shortcuts import render
import django.views.generic as generic
# Create your views here.

class AboutView(generic.TemplateView):
    template_name = "controller/about.html"
