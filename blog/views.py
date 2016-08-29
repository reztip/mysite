from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context = {'posts': posts})

def detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/detail.html', context = {'post': post})

def edit(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
         new_text = request.POST.get('post_body', False)
         if new_text:
             post.body = new_text
             post.save()
             return redirect(reverse('blog:detail', args=(post.id,)))
         else:
            return render(request, 'blog/edit.html', context = {'post': post})
    else:
        return render(request, 'blog/edit.html', context = {'post': post})

