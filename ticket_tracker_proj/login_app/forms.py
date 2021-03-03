from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import fields
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import User
import re

class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'password', 'birthday']

    # def clean_first_name(value):
    #     print("**" * 50)
    #     print(value)
    #     print("**" * 50)
    #     first_name_regex = re.compile(r"^[A-Z]{1}[a-zA-Z]+$")
    #     if first_name_regex.match(value):
    #         return value
    #     if len(value) < 2:
    #         print('Must contain at least 2 characters')
    #         raise forms.ValidationError("First name must be at leased 2 characters long.")
    #     else:
    #         print('First name must begin with a capital')
    #         raise forms.ValidationError("First name must begin with a capital")

    # def clean_last_name(value):
    #     last_name_regex = re.compile(r"^[a-zA-Z]+$")
    #     if last_name_regex.match(value):
    #         return value
    #     if len(value) < 2:
    #         print('Must contain at least 2 characters')
    #         raise forms.ValidationError("Last name must be at leased 2 characters long.")
    #     else:    
    #         print('Last name must consist only of letters')
    #         raise forms.ValidationError("Last name must consist only of letters.")
        
    # def clean_email_address(value):
    #     email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    #     if email_regex.match(value):
    #         return value
    #     if not email_regex.match(value):
    #         print('Invalid email address')
    #         raise forms.ValidationError("Invalid email address.")
    #     try:
    #         User.objects.get(email_address = value)
    #         print('That email is already in use')
    #         raise forms.ValidationError("That email is already in use.")
    #     except:
    #         pass

    # def clean_password(value):
    #     if len(value) < 8:
    #         print("Your password needs to be at least 8 characters long")
    #         raise forms.ValidationError("Your passwords dont match.")

    # def clean_password_confirm(value):
    #     if len(value) < 8:
    #         print("Your password needs to be at least 8 characters long")
    #         raise forms.ValidationError("Your passwords dont match.")



    # def age_validator(self, post_data):
    #     errors = {}
    #     age_limit = datetime.timedelta(days=4745) # 13 years old
    #     in_age = post_data['birthday']
    #     in_age = datetime.datetime.strptime(in_age, "%Y-%m-%d")
    #     today = datetime.datetime.today()
    #     curr_td = today - in_age
    #     if curr_td < age_limit:
    #         raise ValidationError("You are too young to register.  Must be 13 years old.")
    #     # return errors


    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2100)))


    # first_name = forms.CharField(max_length=50, validators=[clean_first_name])
    # last_name = forms.CharField(max_length=50, validators=[clean_last_name])
    # email_address = forms.EmailField(validators=[clean_email_address])
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[clean_password])
    # confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[clean_password_confirm])
    # birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2100)))

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email_address', 'password']
    email_address = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
