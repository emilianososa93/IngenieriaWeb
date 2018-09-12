from django.conf.urls import  url,include
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

urlpatterns = [
		url(r'^$', views.post_portada, name='post_portada'),
		url(r'^post/$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/detail/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/login/$', views.post_login, name ='post_login'),
        url(r'^post/registro/$', views.post_registro, name ='post_registro'),
        url(r'^post/portada/$', views.post_portada, name ='post_portada'),
]