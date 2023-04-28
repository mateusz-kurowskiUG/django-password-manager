from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth.models import User
from passwd_manager_app.models import User_avatar
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method=="POST":
        registrationForm = forms.RegisterForm(response.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            username = registrationForm.cleaned_data["username"]
            user = User.objects.get(username=username)
            new_avatar = User_avatar(user=user,avatar=r"passwd_manager_app\files\avatars\mariusz_z_mieczem.jpg")
            new_avatar.save()
            messages.info(response,"You have been successfully registered")
            return redirect("/login/")
        else:
            registrationForm = forms.RegisterForm()
            return render(response,"registration/register.html",{"form":registrationForm})
            
    else:
        registrationForm = forms.RegisterForm()
    return render(response,"registration/register.html",{"form":registrationForm})