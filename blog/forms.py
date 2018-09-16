from django import forms
from .models import Post, Login

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')



class PostLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')




    