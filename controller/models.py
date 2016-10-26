from django.db import models
from django import forms
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length = 30)
    location = models.FileField(upload_to = 'projects/', default = 'under_construction.html')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput, required = True)
    email = forms.CharField(max_length = 75, required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
