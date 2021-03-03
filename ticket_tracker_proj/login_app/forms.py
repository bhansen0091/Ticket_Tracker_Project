from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import User


# class RegistrationForm(forms.Form):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email_address', 'password', 'birthday']
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email_address = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     birthday = forms.DateField()

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'password', 'birthday']

        widgets = {
            "first_name": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'First Name',
                }),
            "last_name": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            "email_address": forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Email Address'
                }),
            "password": forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "birthday": forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
            })
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email_address', 'password']

        widgets = {
            'email_address': forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Email Address'
                }),
            'password': forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }
