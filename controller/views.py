from django.shortcuts import render
from django.http import HttpResponse
import django.views.generic as generic
import os

class AboutView(generic.TemplateView):
    template_name = "controller/about.html"

def resume_view(request):
    with open('./controller/static/controller/resume.pdf', 'rb') as pdf:
        response = HttpResponse(content = pdf)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename = resume.pdf'
        return response



class ResumeView(generic.TemplateView):
    template_name = "controller/resume.html"

class BlogView(generic.TemplateView):
    template_name = "controller/blog.html"

class ProjectsView(generic.TemplateView):
    template_name = "controller/projects.html"

class OtherView(generic.TemplateView):
    template_name = "controller/other.html"

class HomeView(generic.TemplateView):
    template_name = "controller/home.html"
    
