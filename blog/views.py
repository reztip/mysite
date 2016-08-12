from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context = {'posts': posts})

def detail(request, pk):
    pass
