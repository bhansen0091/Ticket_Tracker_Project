from django.shortcuts import render, redirect

#----- Display Dashboard showing all tasks --------------------------

def dashboard(request):
    return render(request, "dashboard.html")

#------------------- Create New Task --------------------------------

def new_task(request):
    return render(request, "create_task.html")

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
