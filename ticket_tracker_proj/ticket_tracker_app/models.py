from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
from django.forms.fields import CharField
from login_app.models import User



class Subtask(models.Model):
    name = models.CharField(max_length=510)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    sub_created_by = models.ForeignKey(User, related_name="created_sub_tasks", on_delete=CASCADE)
    sub_contributors = models.ManyToManyField(User, related_name="sub_tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # need to add validations form forms view

class Task(models.Model):
    name = models.CharField(max_length=510)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name="created_tasks", on_delete=CASCADE)
    contributors = models.ManyToManyField(User, related_name="tasks")
    subtasks = models.ForeignKey(Subtask, null=True, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # need to add validations form forms view




