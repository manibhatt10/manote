from django.shortcuts import render

# Create your views here.
from .models import Task

def task_list(request):
    tasks=Task.objects.all()  #fetches all from DB
    return render(request, 'tasks/task_list.html',{'tasks':tasks})
'''Task.objects.all(): This is Django's ORM (Object-Relational Mapper) talking to the database for you.

render(): This function combines a template with a "context" dictionary (the {'tasks': tasks} part) to create the final HTML.'''