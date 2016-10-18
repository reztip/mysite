from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import django.views.generic as generic
from django.contrib.auth import authenticate, login, logout

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

def login_view(request):
    if request.method == "GET":
        return render(request, "controller/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            url = reverse('home')
            return HttpResponseRedirect(url)
        else:
            return render(request, "controller/login.html", context = {
                'failure': True
                })

def logout_view(request):
    if request.user:
        logout(request)
        url = reverse('home')
    else:
        url = request.path
    return HttpResponseRedirect(url)
        
def register_view(request):
    if request.user:
        return HttpResponseRedirect(reverse('login'))
    if request.user:
        logout(request)
        url = reverse('home')
    else:
        url = request.path
    return HttpResponseRedirect(url)


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
    
