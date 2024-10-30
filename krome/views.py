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

@login_required(login_url='login')
def kfmembers(request):
    return render(request,'kfmembers.html')

@login_required(login_url='login')
def kspmembers(request):
    return render(request,'kspmembers.html')

@login_required(login_url='login')
def kspchallenge(request):
    return render(request,'ksp6week/homepage.html')

@login_required(login_url='login')
def intro6wk(request):
    return render(request,'ksp6week/intro6wk.html')

def ksphome(request):
    return render(request,'ksp_home.html')

def kfprograms(request):
    return render(request,'kfprograms.html')

@login_required(login_url='login')
def kfmemprog(request):
    return render(request,'kfmemprog.html')

@login_required(login_url='login')
def kspmemprog(request):
    return render(request,'kspmemprog.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render (request, 'logout.html')  

@login_required(login_url='login')
def monday(request):
    return render(request,'ksp6week/monday.html')

@login_required(login_url='login')
def tuesday(request):
    return render(request,'ksp6week/tuesday.html')

@login_required(login_url='login')
def wednesday(request):
    return render(request,'ksp6week/wednesday.html')

@login_required(login_url='login')
def thursday(request):
    return render(request,'ksp6week/thursday.html')

@login_required(login_url='login')
def friday(request):
    return render(request,'ksp6week/friday.html')

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

def shop(request):
    return render(request,'shop.html')


@login_required(login_url='login')
def kfmemshop(request):
    return render(request,'kfmemshop.html')

@login_required(login_url='login')
def kspshop(request):
    return render(request,'kspshop.html')


def strength(request):
    return render(request,'strength.html')

@login_required(login_url='login')
def mw(request):
    return render(request,'m_w.html')

@login_required(login_url='login')
def tt(request):
    return render(request,'t_t.html')

@login_required(login_url='login')
def challenges(request):
    return render(request,'challenges.html')

def transformation(request):
    return render(request,'transformation.html')

 



