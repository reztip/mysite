from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Project(models.Model):
    name = models.CharField(max_length = 30)
    location = models.FileField(upload_to = 'projects/', default = 'under_construction.html')

class UserForm(UserCreationForm):
    email = forms.CharField(max_length = 75, required = True)
    password1 = forms.CharField(max_length = 50, required = True, 
            widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 50, required = True, 
            widget = forms.PasswordInput)
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']
