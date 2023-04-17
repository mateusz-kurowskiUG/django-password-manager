from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden
from .forms import NewPasswordForm, EditItem,DeleteItem
from .models import Accounts, User
from django.contrib import messages
from registration.forms import DeleteAcc,EditPassword

def home(response):
    return render(response,'main/home.html',{})

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
                messages.info(response,"Your password has been added")
                form = NewPasswordForm()
                
        else:
            form = NewPasswordForm()
        return render(response,"main/add_new.html",{"form":form})
    
def my_password(response,id):
    try:
        acc_from_db = Accounts.objects.get(id=id)
    except Accounts.DoesNotExist:
        return render(response,"main/question_mark.html",{})
    else:
        if response.user != acc_from_db.user:
            return render(response,"main/question_mark.html",{})

        
        if response.method=="POST":
            if 'update' in response.POST:
                Edit = EditItem(response.POST)
                if Edit.is_valid():
                    acc_from_db.acc_name = Edit.cleaned_data["acc_name"]
                    acc_from_db.login = Edit.cleaned_data["login"]
                    acc_from_db.password = Edit.cleaned_data["password"]
                    acc_from_db.save()
                    messages.info(response,"Your password has been UPDATED")
                    Edit = EditItem()
                    Delete = DeleteItem()
            elif 'delete' in response.POST:
                Delete = DeleteItem(response.POST)
                if Delete.is_valid():
                        if Delete.cleaned_data["sure"] == True:
                            acc_from_db.delete()
                            messages.info(response,"Your password has been DELETED")
                            return HttpResponseRedirect("/home")
                                
        Edit = EditItem()
        Delete = DeleteItem()
        return render(response,'main/pass.html',{"acc_from_db":acc_from_db,"edit_form":Edit,"delete_form":Delete})
            

def signed_out(response):
    return render(response,'registration/logout.html',{})

def my_account(response,username):
    if username != response.user.username:
            return HttpResponseForbidden()
    else:
        if response.method=="POST":
            if "delete_acc" in response.POST:
                deletion_form = DeleteAcc(response.POST)
                if deletion_form.is_valid():
                    user = User.objects.get(username=username)
                    user.delete()
                    messages.info(response,"Your account has been deleted")
                    return HttpResponseRedirect("/home")
            elif "edit_password" in response.POST:
                edit_form = EditPassword(response.POST)
                if edit_form.is_valid():
                    old_passwd = edit_form.cleaned_data["old_password"]
                    new_passwd = edit_form.cleaned_data["new_password"]
                    if old_passwd == response.user.password:
                        user = User.objects.get(username=response.user.username)
                        user.password = new_passwd
                        user.save()
                        messages.info(response,"Your password has been successfully changed")

                    else:
                        messages.info(response,"Incorrect old password")

        
        edit_form = EditPassword()
        deletion_form = DeleteAcc()
        return render(response,"main/my_acc.html",{"deletion_form":deletion_form,"edit_form":edit_form})
        
    