from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render , redirect
from .forms import PostForm, UserForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
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

@login_required
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


class post_login(View):

    form_class = UserForm

    def get(self,request):
        form = self.form_class(None)
        return render(request, 'blog/post_login.html', {'form': form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                #revisar que controle que la contraseña ingresada sea la correcta.
                if User.objects.filter(password=form.cleaned_data['password']) == (User.objects.filter(username=form.cleaned_data['username']).password):
                    user = form.save(commit=False)
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        if user.is_active:
                            login(request,user)
                        return redirect('post_portada')
                else:
                    messages.success(request, "Usuario/Contraseña ingresado no es valido ")
            else:
                messages.success(request, "Usuario/Contraseña ingresado no es valido ")
        return render(request, 'blog/post_login.html', {'form': form})

class post_registro(View):
    form_class = RegisterForm

    def get(self,request):
        form = self.form_class(None)
        return render(request, 'blog/post_registro.html', {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                if not User.objects.filter(email=form.cleaned_data['email']).exists():
                    if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                    
                        user = form.save(commit=False)
                        username = form.cleaned_data['username']
                        email = form.cleaned_data['email']
                        password1 = form.cleaned_data['password1']
                        password2 = form.cleaned_data['password2']
                        nombre = form.cleaned_data['nombre']
                        apellido = form.cleaned_data['apellido']


                        user = User.objects.create_user(username=username, password=password1,email=email,first_name=nombre,last_name=apellido)
                        user.save()

                        if user is not None:
                            if user.is_active:
                                #esta linea es para solucionar el error de backedn
                                user.backend = 'django.contrib.auth.backends.ModelBackend'
                                #########
                                login(request,user)
                            return redirect('post_portada')
                    
                    else:
                        messages.success(request, "Las contraseñas ingresadas no son iguales")
                else:
                    messages.success(request, "El correo ingresado ya esta asociado a una cuenta")
            else:
                messages.success(request, "El Usuario ingresado ya se encuentra registrado.")
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

@login_required
def logout(request):
    try:
        print("ok")
        auth_logout(request)
    except Exception as e:
        print(e)
    return HttpResponseRedirect("/")

