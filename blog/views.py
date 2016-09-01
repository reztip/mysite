from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from .models import Post
from .forms import PostForm, PostSearchForm

def index(request):
    posts = Post.objects.all()
    # searchform  = PostSearchForm()
    return render(request, 'blog/index.html', context = {
        'posts': posts,
        # 'searchform': searchform, 
        })

def detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/detail.html', context = {'post': post})

def edit(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
         new_text = request.POST.get('post_body', False)
         new_title = request.POST.get('post_title', False)
         if new_text and new_text:
             post.body = new_text
             post.title = new_title
             post.save()
             return redirect(reverse('blog:detail', args=(post.id,)))
         else:
            return render(request, 'blog/edit.html', context = {'post': post})
    else:
        return render(request, 'blog/edit.html', context = {'post': post})


def search(request):
    post_title = request.GET.get('post_title', False)
    post_body = request.GET.get('post_body', False)
    if post_title:
        post_title = post_title.strip()
    if post_body:
        post_body = post_body.strip()

    if post_title or post_body:
        if post_title and post_body:
            titles = Post.objects.filter(title__icontains = post_title)
            bodies = Post.objects.filter(body__icontains = post_body)
            query = titles | bodies
            return render(request, 'blog/search.html', context = {
                "posts": query,
                'post_title': post_title,
                'post_body': post_body,
                })

        if post_body:
            query = Post.objects.filter(body__icontains = post_body)
            return render(request, 'blog/search.html', context = {
                'post_title': post_title,
                'post_body': post_body,
                "posts": query
                })

        else:
            query = Post.objects.filter(title__icontains = post_title)
            return render(request, 'blog/search.html', context = {
                'post_title': post_title,
                'post_body': post_body,
                "posts": query
                })
    else:
        return render(request, 'blog/index.html')

     
