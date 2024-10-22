from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from kromefitness import settings
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from krome import forms
from .models import Athlete

# Create your views here.
def index(request):
    return render (request, 'index.html')

def kromehome(request):
    return render(request, 'krome_home.html')

def about(request):
    return render(request,'about.html')

def conditioning(request):
    return render(request,'conditioning.html')

def flexmob(request):
    return render(request,'flexmob.html')

def kromereg(request):
    return render(request,'krome_reg.html')

def ksphome(request):
    return render(request,'ksp_home.html')

def login(request):
    return render(request,'login.html')
def logout(request):
    return render (request, 'logout.html')  

def mw(request):
    return render(request,'m_w.html')

def meals(request):
    return render(request,'meals.html')

def password_reset(request):
    return render (request, 'password_reset.html') 

def password_reset_complete(request):
    return render (request, 'password_reset_complete.html')

def password_reset_confirm(request):
    return render (request, 'password_reset_confirm.html')

def password_reset_done(request):
    return render (request, 'password_reset_done.html')

def programonline(request):
    return render(request,'program_online.html')
@login_required(login_url='login')


def shop(request):
    return render(request,'shop.html')

def strength(request):
    return render(request,'strength.html')

def tt(request):
    return render(request,'t_t.html')

def transformation(request):
    return render(request,'transformation.html')

 



