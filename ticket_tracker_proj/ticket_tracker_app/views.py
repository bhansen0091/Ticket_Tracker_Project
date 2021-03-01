from django.shortcuts import render, redirect

#----- Display Dashboard showing all tasks --------------------------

def dashboard(request):
    return render(request, "dashboard.html")

#--------------------------------------------------------------------
