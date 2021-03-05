from django.shortcuts import render, redirect
from .models import Task, Subtask
from login_app.models import User
from .forms import CreateSubTask, CreateTask, EditTask, EditSubTask

#----- Display Dashboard showing all tasks --------------------------

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        "user": user,
    }
    try:
        context['tasks'] = user.created_tasks.all()
        cur_task = Task.objects.get(id=request.session['task_id'])
        context['current_task'] = cur_task
        context['sub_tasks'] = cur_task.subtasks.all()
        context['contributions'] = user.con_tasks.all()
        if cur_task.filter(contributors=user) > 0:
            context['remove_self_contrib'] = True
        # print(context['current_task'])
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
    user = User.objects.get(id=request.session['user_id'])
    new_task = Task.objects.create(
        name = request.POST['name'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        description = request.POST['description'],
        created_by = user
    )
    return redirect("/dashboard")

#------------------- Edit Task --------------------------------------

def edit_task(request, task_id):
    this_task = Task.objects.get(id = task_id)
    edit_form = EditTask(instance=this_task)

    if request.method == "POST":
        edit_form = EditTask(request.POST, instance=this_task)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("/dashboard")

    context = {
        "edit_form": edit_form,
        "this_task": this_task,
    }
    return render(request, "edit_task.html", context)

#------------------- Create New Subtask -----------------------------

def new_subtask(request, task_id):
    this_task = Task.objects.get(id = task_id)
    add_sub_form = CreateSubTask()

    context = {
        "current_task": this_task,
        "add_sub_form": add_sub_form,
    }
    return render(request, "add_subtask.html", context)

def create_subtask(request, task_id):
    user = User.objects.get(id = request.session['user_id'])
    this_task = Task.objects.get(id = task_id)

    new_sub = Subtask.objects.create(
        name = request.POST['name'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        description = request.POST['description'],
        sub_created_by = user,
        parent_task = this_task
    )
    return redirect("/dashboard")

#------------------- Edit Subtask -----------------------------

def edit_subtask(request, task_id, subtask_id):
    this_task = Task.objects.get(id = task_id)
    this_sub = Subtask.objects.get(id = subtask_id)

    edit_sub_form = EditSubTask(instance=this_sub)

    if request.method == "POST":
        edit_sub_form = EditSubTask(request.POST, instance=this_sub)
        if edit_sub_form.is_valid():
            edit_sub_form.save()
            return redirect("/dashboard")

    context = {
        "edit_sub_form": edit_sub_form,
        "this_task": this_task,
        "this_sub": this_sub,
    }
    return render(request, "edit_subtask.html", context)


def render_task_id(request, task_id):
    print("**" * 50)
    request.session['task_id'] = task_id
    return redirect('/dashboard')

#------------------- Delete Task & Subtask --------------------

def delete_task(request, task_id):
    Task.objects.get(id = task_id).delete()
    return redirect("/dashboard")
    
def delete_subtask(request, task_id, subtask_id):
    Subtask.objects.get(id = subtask_id).delete()
    return redirect("/dashboard")

#------------------- Contributors -----------------------------

def view_contributors(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "contributors": user.con_tasks.all(),
        "task": user.created_tasks.all()
    }
    
    return render(request, "contributors.html", context)

def add_contributor(request, task_id):
    this_task = Task.objects.get(id = task_id)
    user = User.objects.get(id = request.session['user_id'])
    this_task.contributors.add(user)
    return redirect("/dashboard")

#------------------- Open Projects -----------------------------

def open_tasks(request):
    user = User.objects.get(id = request.session['user_id'])
    not_my_projects = Task.objects.exclude(created_by = user)
    not_my_contributions = Task.objects.exclude(contributors = user)
    
    context = {
        "user": user,
        "not_my_projects": not_my_projects,
        "not_my_contribs": not_my_contributions
    }
    return render(request, "open_projects.html", context)














# from ticket_tracker_app.models import Task, Subtask
# from login_app.models import User

# daniel = User.objects.get(id=2)
# brandon = User.objects.get(id=1)
# james = User.objects.get(id=3)

# d_task1 = Task.objects.create(name="First Task d", start_date="2021-06-06", end_date="2022-07-07", description="This is the first task description d", created_by=daniel)
# d_task2 = Task.objects.create(name="Second Task d", start_date="2021-06-06", end_date="2022-07-07", description="This is the second task description d", created_by=daniel)
# d_task3 = Task.objects.create(name="Third Task d", start_date="2021-06-06", end_date="2022-07-07", description="This is the Third task description d", created_by=daniel)
# d_task1 = Task.objects.get(id=1)
# d_task2 = Task.objects.get(id=2)
# d_task1.contributors.add(brandon)
# d_task1.contributors.add(james)
# d_task2.contributors.add(james)
# d_task2.contributors.add(brandon)
# d_subtask1 = Subtask.objects.create(name="First subtask d", start_date="2021-04-04", end_date="2021-05-05", description="First subtask description d", sub_created_by=daniel, parent_task=d_task1)
# d_subtask2 = Subtask.objects.create(name="Second subtask d", start_date="2021-04-04", end_date="2021-05-05", description="Second subtask description d", sub_created_by=daniel, parent_task=d_task1)
# d_subtask3 = Subtask.objects.create(name="Third subtask d", start_date="2021-04-04", end_date="2021-05-05", description="Third subtask description d", sub_created_by=daniel, parent_task=d_task1)


# b_task1 = Task.objects.create(name="First Task b", start_date="2021-06-06", end_date="2022-07-07", description="This is the first task description b", created_by=brandon)
# b_task2 = Task.objects.create(name="Second Task b", start_date="2021-06-06", end_date="2022-07-07", description="This is the second task description b", created_by=brandon)
# b_task3 = Task.objects.create(name="Third Task b", start_date="2021-06-06", end_date="2022-07-07", description="This is the Third task description b", created_by=brandon)
# b_task1 = Task.objects.get(id=4)
# b_task2 = Task.objects.get(id=5)
# b_task1.contributors.add(daniel)
# b_task1.contributors.add(james)
# b_task2.contributors.add(james)
# b_task2.contributors.add(daniel)
# b_subtask1 = Subtask.objects.create(name="First subtask b", start_date="2021-04-04", end_date="2021-05-05", description="First subtask description b", sub_created_by=brandon, parent_task=b_task1)
# b_subtask2 = Subtask.objects.create(name="Second subtask b", start_date="2021-04-04", end_date="2021-05-05", description="Second subtask description b", sub_created_by=brandon, parent_task=b_task1)
# b_subtask3 = Subtask.objects.create(name="Third subtask b", start_date="2021-04-04", end_date="2021-05-05", description="Third subtask description b", sub_created_by=brandon, parent_task=b_task1)


# j_task1 = Task.objects.create(name="First Task j", start_date="2021-06-06", end_date="2022-07-07", description="This is the first task description j", created_by=james)
# j_task2 = Task.objects.create(name="Second Task j", start_date="2021-06-06", end_date="2022-07-07", description="This is the second task description j", created_by=james)
# j_task3 = Task.objects.create(name="Third Task j", start_date="2021-06-06", end_date="2022-07-07", description="This is the Third task description j", created_by=james)
# j_task1 = Task.objects.get(id=5)
# j_task2 = Task.objects.get(id=7)
# j_task1.contributors.add(daniel)
# j_task1.contributors.add(brandon)
# j_task2.contributors.add(brandon)
# j_task2.contributors.add(daniel)
# j_subtask1 = Subtask.objects.create(name="First subtask j", start_date="2021-04-04", end_date="2021-05-05", description="First subtask description j", sub_created_by=james,  parent_task=j_task1)
# j_subtask2 = Subtask.objects.create(name="Second subtask j", start_date="2021-04-04", end_date="2021-05-05", description="Second subtask description j", sub_created_by=james,  parent_task=j_task1)
# j_subtask3 = Subtask.objects.create(name="Third subtask j", start_date="2021-04-04", end_date="2021-05-05", description="Third subtask description j", sub_created_by=james,  parent_task=j_task1)




