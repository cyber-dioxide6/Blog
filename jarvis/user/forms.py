from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
import re

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("Passwords cannot contain special characters (!@#$%^&*(),.?\":{}|<>).")
        return password

class postform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'post', 'image', 'category', 'summary']