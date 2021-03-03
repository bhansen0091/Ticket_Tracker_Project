from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import LoginForm, RegistrationForm
import bcrypt

def index(request):

    reg_form = RegistrationForm()
    logn_form = LoginForm()
    context = {
        'registration_form': reg_form,
        'login_form': logn_form
    }
    return render(request, "index.html", context)

# --------------- User Registration ---------------

def register(request):
    reg_errors = User.objects.basic_validator(request.POST)
    if len(reg_errors) > 0:
        for key, value in reg_errors.items():
            messages.error(request, value)
        return redirect('/')

    if request.method == "POST":
        bound_reg_form = RegistrationForm(request.POST)
        print("*" *100)
        print(request.POST)
        print("*" *100)
        # print('bound_reg_form.is_Valid(): ', bound_reg_form)
        # print('bound_reg_form.errors: ' , bound_reg_form.errors)
        # # print('clean_data' , bound_reg_form.cleaned_data)
        if bound_reg_form.is_valid():
            # bound_reg_form.full_clean()
            # print(bound_reg_form.is_valid())
            pw_hash = bcrypt.hashpw(bound_reg_form.cleaned_data['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=bound_reg_form.cleaned_data['first_name'], last_name=bound_reg_form.cleaned_data['last_name'], birthday=bound_reg_form.cleaned_data['birthday'], email_address=bound_reg_form.cleaned_data['email_address'], password=pw_hash)
    return redirect('/')

# --------------- User Login ---------------

def login(request):
    # try:
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == "POST":
        bound_logn_form = LoginForm(request.POST)
        if bound_logn_form.is_valid():
            cur_email = bound_logn_form.cleaned_data['email_address']
            try:
                user = User.objects.get(email_address = cur_email)
            except:
                messages.error(request, "Email does not exist")
                return redirect('/')

            if not bcrypt.checkpw(bound_logn_form.cleaned_data['password'].encode(), user.password.encode()):
                print('redirecting....')
                messages.error(request, "Invalid email or password.")
                return redirect("/")

        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['email'] = user.email_address
        return redirect("/dashboard")

# --------------- User Logout ---------------

def logout(request):
    request.session.clear()
    return redirect("/")