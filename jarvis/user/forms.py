from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
import re
from django.contrib.auth.models import User

#User Registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
#Create a post Form
class postform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'post', 'image', 'category', 'summary']

#Edit Profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # or CustomUser if extending directly
        fields = ['bio', 'profile_picture']
        

        