from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    return render(request, 'blog/index.html', context = {'posts': paginator.page(1)})

def detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/detail.html', context = {'post': post})
