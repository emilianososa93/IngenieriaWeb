from django import forms
from .models import Post
from django.contrib.auth import (logout, login, authenticate, get_user_model)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

user = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
    	username = self.cleaned_data.get("username")
    	password = self.cleaned_data.get("password")
    	user = authenticate(username=username,password=password)
    	if not user:
    		raise forms.ValidationError("Tu usuario no existe")
    	if not user.checked_password(password):
    		raise forms.ValidationError("Contraseña incorrecta")
    	if not user.is_active:
    		raise forms.ValidationError("El usuario no se encuentra activo")
    	return super(Login,self).clean(*args,**kwargs)	
