from django.db import models
from django.utils import timezone
from django.contrib.auth import (logout, login, authenticate)
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Login(models.Model):
    username = models.ForeignKey('auth.User',on_delete = models.CASCADE, null=True, blank=True,max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username
