from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
        
class DeleteAcc(forms.Form):
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
    sure = forms.BooleanField(required=True,label="U sure?")
    
class EditPassword(forms.Form):
    old_password = forms.CharField(label="Old Password",widget=forms.PasswordInput())
    new_password = forms.CharField(label="New Password",widget=forms.PasswordInput())
