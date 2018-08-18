from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_them_login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^post/login/$', views.post_login, name ='logout'),
]