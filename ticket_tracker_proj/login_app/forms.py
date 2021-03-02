from django import forms
from django.forms import fields
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from . import User


class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'password', 'birthday']
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    birthday = forms.DateField()


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email_address', 'password']
    email_address = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
