from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
from django.forms.fields import CharField
from login_app.models import User




class Task(models.Model):
    name = models.CharField(max_length=510)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name="created_tasks", on_delete=CASCADE)
    contributors = models.ManyToManyField(User, related_name="con_tasks") # THROUGH CON_APPROVED (Approved =>True Approval_Needed => False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # need to add validations form forms view

class Subtask(models.Model):
    name = models.CharField(max_length=510)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    sub_created_by = models.ForeignKey(User, related_name="created_sub_tasks", on_delete=CASCADE)
    sub_contributors = models.ManyToManyField(User, related_name="con_sub_tasks") # THROUGH SUB_CON_APPROVED (Approved => True  Approval_Needed => False)
    parent_task = models.ForeignKey(Task, null=True, related_name="subtasks", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # need to add validations form forms view

# all_tasks = Task.objects.all()
# for this_task in all_tasks:
#     if len(this_task.contributors.all()) > 0:
#         print(f"Task: {this_task.name} {this_task.id}")
#     else:
#         print(f"Contributors:{this_task.name} {this_task.id}")

# {% if this_task.contributors.all|length > 0 %}
# {% endif %}

# class Comment(models.Model):
    # text = models.CharFiel(max_length=510)
    # by = models.ForeignKey(User, related_name="created_comments")
    # attached_task = models.ForeignKey(Task, related_name="task_comments", null=True)
    # attached_subtask = models.ForeignKey(Subtask, related_name="sub_comments", null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
