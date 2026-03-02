from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g buy milk'}),
            'description': forms.Textarea(attrs={'placeholder': 'go to xyz shop'}),
            # You can add one for description here too!
        }

# A full form for the edit page
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']