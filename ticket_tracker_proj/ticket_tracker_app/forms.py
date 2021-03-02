from ticket_tracker_proj.ticket_tracker_app.models import Task
from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from . import User

class CreateTask(forms.Form):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'description', 'sub_contributors']
    name = forms.CharField(max_length=200)
    start_date = forms.DateField()
    end_date = forms.DateField()
    phase = forms.IntegerField()   # singular??
    contributor = forms.ModelMultipleChoiceField() # allow selection of contributors
