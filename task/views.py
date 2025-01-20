from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .form import TaskForm
from django.utils.timezone import now


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks, 'now': now()})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})

# def edit_task(request, pk):
#     task = get_object_or_404(TaskModel, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('show_tasks')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'task/add_task.html', {'form': form})
def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})
def delete_task(request, task_id):
    try:
        task = TaskModel.objects.get(id=task_id)
        task.delete()
        return redirect('show_tasks')
    except TaskModel.DoesNotExist:
        return redirect('show_tasks') 
            
def complete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
