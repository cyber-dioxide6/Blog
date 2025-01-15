from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class postform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'post', 'image', 'category', 'summary']