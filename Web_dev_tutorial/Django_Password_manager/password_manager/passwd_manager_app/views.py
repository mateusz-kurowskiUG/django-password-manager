from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def home(response):
    return render(response,'main/base.html',{})

def passwords(response):
    if response.user.is_authenticated:
        return render(response,'main/passwords.html',{})
    else:
        return redirect("/login")