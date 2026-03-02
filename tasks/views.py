from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm, UserRegisterForm

@login_required
def task_list(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskCreateForm()
    
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

@login_required # Added protection
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user) # Ensure user owns the task
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_confirm.html', {'task': task})

@login_required # Added protection
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user) # Ensure user owns the task
    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('edit_task', pk=task.pk)
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # 1. FIXED: Moved the empty form creation here
        form = UserRegisterForm()

    # 2. FIXED: Moved the return statement out of the 'if' block 
    # so it handles both GET and invalid POST requests.
    return render(request, 'tasks/register.html', {'form': form})