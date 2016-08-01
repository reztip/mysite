from django.shortcuts import render
from django.http import HttpResponse
import django.views.generic as generic

class AboutView(generic.TemplateView):
    template_name = "controller/about.html"

def resume_view(request):
    with open('../static/controller/resume.pdf', 'rb') as pdf:
        print(pdf)
        response = HttpResponse(content = pdf)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename = resume.pdf'
        return response



class ResumeView(generic.TemplateView):
    template_name = "controller/resume.html"

class BlogView(generic.ListView):
    template_name = "controller/blog.html"

class ProjectsView(generic.ListView):
    template_name = "controller/projects.html"

class OtherView(generic.ListView):
    template_name = "controller/other.html"

class HomeView(generic.TemplateView):
    template_name = "controller/home.html"
    
