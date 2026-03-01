from django import forms
from .models import Task





class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

# A full form for the edit page
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']