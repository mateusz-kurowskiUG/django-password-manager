from django import forms

class NewPasswordForm(forms.Form):
    acc_name = forms.CharField(label="Name")
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
