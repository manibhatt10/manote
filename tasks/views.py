from django.shortcuts import render,redirect

# Create your views here.
from .models import Task
from .forms import TaskForm


def task_list(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    #tasks=Task.objects.all()  #fetches all from DB
    tasks=Task.objects.all().order_by('-created_at') #minus sign for descending order
    return render(request, 'tasks/task_list.html',{'tasks':tasks,'form':form})
'''Task.objects.all(): This is Django's ORM (Object-Relational Mapper) talking to the database for you.

render(): This function combines a template with a "context" dictionary (the {'tasks': tasks} part) to create the final HTML.'''