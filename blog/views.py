from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render , redirect
from .forms import PostForm, UserForm, RegisterForm
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect



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

#
#Falta que controle si el usuario que se loguea esta registrado
#El registro funciona
#
class post_login(View):
    form_class = UserForm

    def get(self,request):
        form = self.form_class(None)
        return render(request, 'blog/post_login.html', {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password1)

            if user is not None:
                if user.is_active:
                    login(request,user)
                return redirect('post_portada')
        return render(request, 'blog/post_login.html', {'form': form})

class post_registro(View):
    form_class = RegisterForm

    def get(self,request):
        form = self.form_class(None)
        return render(request, 'blog/post_registro.html', {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            user.set_password(password1)
            user.save()

            user = authenticate(username=username, password=password1)

            if user is not None:
                if user.is_active:
                    login(request,user)
                return redirect('post_portada')
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

def logout(request):
    try:
        print("ok")
        auth_logout(request)
    except Exception as e:
        print(e)
    return HttpResponseRedirect("/")

