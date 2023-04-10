from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.
def register(response):
    if response.method=="POST":
        form = forms.RegisterForm(response.POST)
        if form.is_valid():
            form.save()
                
        return redirect("/")
    else:
        form = forms.RegisterForm()
    return render(response,"registration/register.html",{"form":form})