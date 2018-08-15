from django.shortcuts import render
from django.utils import timezone
from .models import Post
#Aca se detallan las vistas refenreciando al archivo html


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})