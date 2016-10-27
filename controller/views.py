from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
import django.views.generic as generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AnonymousUser, User
from .models import UserForm

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
    url = 'projects/{0}.html'.format(name)
    return render_to_response(url)

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
        
def register_view(request, errors = None):
    # if no user and user is not anonymous, 
    # Redirect home with no warning
    if request.user and not request.user.is_anonymous():
        return HttpResponseRedirect(reverse('home'))
    else:
        # GET => blank register form
        if request.method == "GET":
            userform  = UserForm()
            # pass in an empty user form
            return render(request, 'controller/register.html',
                    context = {'uform': userform,
                        'errors': errors
                        })
        # POST => sign up user, redirect home
        elif request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            new_user = User(username = username, 
                    email = email, password = password)
            try:
                validate_password(password, new_user)
            except ValidationError as err:
                errors = str(err)
                return render(request, "controller/register.html", context = {
                    'errors': errors,
                    })
            # sign up the user in the POST dict
            # using the form fields
            try: 
                try:
                    # user exists already 
                    usr = User.objects.get(username = username)
                    return render(request, 
                            'controller/register.html', context = 
                            {'errors': "user exists already!"})
                except Exception:
                    pass
                new_user.full_clean()
                new_user.save()
                # Send the user a confirm-registration email
                send_mail("Thank you for registering, {0}".format(username),
           'Please remember your password, we have to reset it manually.',
           'alexphi421@gmail.com', [email])
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
            except Exception as e:
                errors = str(e)
                return render(request, "controller/register.html", context = {
                    'errors': errors,
                    })

""" ###########################
#      Class views        #
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
    
