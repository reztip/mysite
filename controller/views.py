from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import django.views.generic as generic
import os
import controller
"""
###########################
Functional views 
###########################
"""
def resume_view(request):
    with open('./controller/static/controller/resume.pdf', 'rb') as pdf:
        response = HttpResponse(content = pdf)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename = resume.pdf'
        return response


def projects_view(request):
    template_name = "controller/projects.html"
    projects = ['titanic', 'digits']
    return render(request, template_name, context = {
        'projects': projects, 
        })

def project_detail_view(request, name):
    location = 'projects/{0}.html'.format(name)
    return render_to_response(location)


"""
###########################
Class views 
###########################
"""
class AboutView(generic.TemplateView):
    template_name = "controller/about.html"

class ResumeView(generic.TemplateView):
    template_name = "controller/resume.html"

class BlogView(generic.TemplateView):
    template_name = "controller/blog.html"

class OtherView(generic.TemplateView):
    template_name = "controller/other.html"

class HomeView(generic.TemplateView):
    template_name = "controller/home.html"
    
