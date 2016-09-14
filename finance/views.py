from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import UserForm

@login_required
def index(request):
    return HttpResponse("{0}".format(request.user))

def login(request):
    pass

def logout(request):
    pass

def new_user(request):
    uform = UserForm()
    return render(request, 'finance/new_user.html', context = {
      'form': uform,
      })

