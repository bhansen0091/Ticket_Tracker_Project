from ticket_tracker_proj.ticket_tracker_app.models import Task
from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from . import User

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'description', 'contributors', 'subtasks']
        widgets = {
            "name": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Task Name',
                }),
            "start_date": forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
            }),
            "end_date": forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
                }),
            "description": forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Task Description'
            }),
            "contributors": forms.ModelMultipleChoiceField(attrs = {
                'class': 'form-control',
                }),
            "subtasks": forms.ModelMultipleChoiceField(attrs = {
                'class': 'form-control',
            })
        }

class CreateSubTask(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['name', 'start_date', 'end_date', 'description', 'contributors', 'subtasks']
        widgets = {
            "name": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Task Name',
                }),
            "start_date": forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
            }),
            "end_date": forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
                }),
            "description": forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Task Description'
            }),
            "sub_contributors": forms.ModelMultipleChoiceField(attrs = {
                'class': 'form-control',
                })
        }