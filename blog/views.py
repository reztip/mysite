from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context = {'posts': posts})

def detail(request, pk):
    post = Post.objects.get(pk = pk)
    # form = PostForm(instance = post)
    return render(request, 'blog/detail.html', context = {'post': post})
