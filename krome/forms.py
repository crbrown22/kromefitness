from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Athlete


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)  
    last_name = forms.CharField(max_length=50)

class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['address', 'phone', 'image']