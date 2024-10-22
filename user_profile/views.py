from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.member = request.user.id
            user.save()
            user_name=form.cleaned_data.get('username')
            #password=form.cleaned_data.get['password1']
            messages.success(request, f'{user_name} has been registered')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'user/register.html', context)


@login_required(login_url='login')
def profile(request):    
    member= User.objects.all()
    
    context={
        'member': member,
              
    }
    return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user_name=user_form.cleaned_data.get('username')
            messages.success(request, f'{user_name} has been updated')
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)
    context={
            'user_form':user_form,
            'profile_form':profile_form
    }
    return render(request, 'user/profile_update.html', context)

@login_required(login_url='login')
def member_delete(request, pk):
    member= User.objects.get(id=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('index')
    return render (request, 'user/member_delete.html')