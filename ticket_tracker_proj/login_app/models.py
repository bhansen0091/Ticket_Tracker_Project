from django.core.exceptions import ValidationError
from django.db import models
import re
import datetime


class UserManager(models.Manager):
    def basic_validator(self, post_data):
        reg_errors = {}
        if not post_data['first_name'].isalpha():
            reg_errors['first_name'] = "First name needs to be letters only"
        if len(post_data['first_name']) < 2:
            reg_errors['first_name'] = "First name should be at least 2 characters long"
        
        if not post_data['last_name'].isalpha():
            reg_errors['last_name'] = "Last name needs to be letters only"
        if len(post_data['last_name']) < 2:
            reg_errors['last_name'] = "Last name should be at least 2 characters long"

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email_address']):
            reg_errors['email_address'] = "Invalid Email address"
        if User.objects.filter(email_address=post_data['email_address']):
            reg_errors['email_address'] = "Email address already exists"

        age_limit = datetime.timedelta(days=4745) # 13 years old
        birthday = f"{post_data['birthday_year']}-{post_data['birthday_month']}-{post_data['birthday_day']}"
        print(birthday)
        print(len(birthday))
        if len(birthday) != 0:
            if len(birthday) < 7:
                print('inside birthday length')
                reg_errors['birthday'] = "Incorrect birthday entered"
            else:
                in_age = birthday
                in_age = datetime.datetime.strptime(in_age, "%Y-%m-%d")
                today = datetime.datetime.today()
                curr_td = today - in_age
                print('passed age verifi')
                if curr_td < age_limit:
                    reg_errors['birthday'] = "You are too young to register.  Must be 13 years old."
        else:
            reg_errors['birthday'] = "Cannot leave date blank"

        pass_regex = re.compile(r'^[a-zA-Z0-9]{8,}')
        if not re.fullmatch(pass_regex, post_data['confirm_password']):
            reg_errors['confirm_password'] = "Password is not at least 8 characters long"
        if post_data['confirm_password'] != post_data['password']:
            reg_errors['confirm_password'] = "Passwords dont match!"

        return reg_errors
    
    def login_validator(self, post_data):
        login_errors = {}
        if len(post_data['email_address']) <= 0:
            login_errors['email_address'] = "Email address cannot be blank"
        if (len(post_data['password'])) <= 0:
            login_errors['password'] = "Password cannot be blank"
        return login_errors


class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    birthday = models.DateField()
    email_address = models.CharField(max_length=320)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()