from ticket_tracker_app.models import Task, Subtask
from django import forms

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'description']
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
            })
        }

class CreateSubTask(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['name', 'start_date', 'end_date', 'description']
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

        }