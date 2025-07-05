# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(title=title)
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Task title cannot be empty!')
    return render(request, 'tasks/task_form.html')

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            task.title = title
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Task title cannot be empty!')
    return render(request, 'tasks/task_form.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    status = 'completed' if task.completed else 'marked as incomplete'
    messages.success(request, f'Task "{task.title}" {status}!')
    return redirect('task_list')

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    messages.success(request, f'Task "{task.title}" marked as complete!')
    return redirect('task_list')

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})