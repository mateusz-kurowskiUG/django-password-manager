from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden
from .forms import NewPasswordForm
from .models import Accounts
from django.contrib import messages
def home(response):
    return render(response,'main/base.html',{})

def passwords(response):
    if response.user.is_authenticated:
        ls = Accounts.objects.filter(user=response.user)
        return render(response,'main/passwords.html',{"ls":ls})
    else:
        return redirect("/login")
    
    
def add_new(response):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        if response.method=="POST":
            form = NewPasswordForm(response.POST)
            if form.is_valid():
                acc_name = form.cleaned_data["acc_name"]
                login = form.cleaned_data["login"]
                password = form.cleaned_data["password"]
                new = Accounts(acc_name=acc_name,login=login,password=password)
                new.save()
                response.user.accounts.add(new)
                messages.info(response,"Twoje hasło jest bezpieczne")
                form = NewPasswordForm()
                
        else:
            form = NewPasswordForm()
        return render(response,"main/add_new.html",{"form":form})