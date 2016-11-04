from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from controller.views import login_view as login_view_controller
from .models import UserForm

@login_required
def index(request):
    return render(request, 'finance/home.html')

def login(request):
    return login_view_controller(request)

def logout(request):
    pass

def new_user(request):
    uform = UserForm()
    return render(request, 'finance/new_user.html', context = {
      'form': uform,
      })

