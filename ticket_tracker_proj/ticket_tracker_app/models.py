from django.db import models
from django.db.models.deletion import CASCADE
from login_app.models import User



class Task(models.Model):
    name = models.CharField(max_length=510)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name="created_tasks", on_delete=CASCADE)
    contributors = models.ManyToManyField(User, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#-- Lay groundwork for Task/subtask relationship -------------------
#-- Using a general tree data structure ----------------------------

class TaskTree:
    def __init__(self, task):
        self.task = task
        self.subtasks = []
        self.parent_task = None

    def add_subtask(self, subtask):
        subtask.parent_task = self
        self.subtasks.append(subtask)

    def get_task_level(self):
        task_level = 0
        parent_task = self.parent_task
        while parent_task:
            task_level += 1
            parent_task = parent_task.parent_task
        return task_level
