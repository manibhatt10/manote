from django.shortcuts import render,redirect

# Create your views here.
from .models import Task
from .forms import TaskCreateForm
from .forms import TaskUpdateForm


def task_list(request):
    if request.method=='POST':
        form=TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskCreateForm()
    #tasks=Task.objects.all()  #fetches all from DB
    tasks=Task.objects.all().order_by('-created_at') #minus sign for descending order
    return render(request, 'tasks/task_list.html',{'tasks':tasks,'form':form})
'''Task.objects.all(): This is Django's ORM (Object-Relational Mapper) talking to the database for you.

render(): This function combines a template with a "context" dictionary (the {'tasks': tasks} part) to create the final HTML.'''

from django.shortcuts import get_object_or_404 # Add this import

def delete_task(request, pk):
    task=get_object_or_404(Task,id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_confirm.html',{'task':task})

def edit_task(request, pk):
    task=get_object_or_404(Task,id=pk)
    if request.method=="POST":
        form=TaskUpdateForm(request.POST,instance=task)# 'instance=task' tells Django to update this specific record
        if form.is_valid():
            form.save()
            return redirect('edit_task', pk=task.pk)
    else:
        form=TaskUpdateForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})