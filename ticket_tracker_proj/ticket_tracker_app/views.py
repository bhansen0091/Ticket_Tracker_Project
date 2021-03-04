from django.shortcuts import render, redirect
from .models import Task, Subtask
from login_app.models import User
from .forms import CreateTask

#----- Display Dashboard showing all tasks --------------------------

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        "user": user,
        "tasks": user.created_tasks.all(),
    }
    try:
        context['current_task'] = Task.objects.get(id=request.session['task_id'])
        print(context['current_task'])
    except:
        pass
    return render(request, "dashboard.html", context)

#------------------- Create New Task --------------------------------

def new_task(request):
    context = {
        "new_task_form": CreateTask()
    }
    return render(request, "create_task.html", context)

def create_task(request):
    return redirect("/dashboard")

#------------------- Edit Task --------------------------------------

def edit_task(request):
    return render(request, "edit_task.html")

def update_task(request):
    return redirect("/dashboard")

#------------------- Create New Subtask -----------------------------

def new_subtask(request):
    return render(request, "add_subtask.html")

def create_subtask(request):
    return redirect("/dashboard")

#------------------- Edit Subtask -----------------------------

def edit_subtask(request):
    return render(request, "edit_subtask.html")

def update_subtask(request):
    return redirect("/dashboard")


def render_task_id(request, task_id):
    print("**" * 50)
    request.session['task_id'] = task_id
    return redirect('/dashboard')