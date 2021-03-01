from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, "index.html")

# --------------- User Registration ---------------

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")

    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        birthday = request.POST['birthday'],
        email_address = request.POST['email_address'],
        password = pw_hash
    )

    messages.info(request, "Registration complete, please login.")
    return redirect("/")

# --------------- User Login ---------------

def login(request):
    try:
        user = User.objects.get(email_address = request.POST['email_address'])
    except:
        messages.error(request, "Invalid email or password.")
        return redirect("/")

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
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