from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import User


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
