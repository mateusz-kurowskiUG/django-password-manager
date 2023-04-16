from django import forms

class NewPasswordForm(forms.Form):
    acc_name = forms.CharField(label="Name")
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())

class EditItem(forms.Form):
    acc_name = forms.CharField(label="Account Name")
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
    
class DeleteItem(forms.Form):
    sure = forms.BooleanField(required=True,label="U sure?")
