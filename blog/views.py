from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User as userAuth
from django.shortcuts import render
from .forms import (PostForm, PostLogin)
from django.shortcuts import redirect
from django.contrib.auth import (logout, login, authenticate, get_user_model)
#Aca se detallan las vistas refenreciando al archivo html


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def post_login(request):
    if request.method == "POST":
        form = PostLogin(request.POST)
        if form.is_valid():
            username = request.username
            password = request.password
            return redirect('post_portada')
    else:
        return render(request, 'blog/post_login.html', {'error': True})
    return render(request, 'blog/post_login.html', {'form': form})

def post_registro(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_registro.html', {'form': form})

def post_portada(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_portada.html', {'form': form})


