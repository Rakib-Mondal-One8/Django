from django.shortcuts import render, redirect
from . import forms
from .models import Task


# Create your views here.
def add(request):
	if request.method == 'POST':
		form = forms.TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	form = forms.TaskForm()
	return render(request, 'task_add.html', {'form': form})


def edit(request, id):
	task = Task.objects.get(id=id)
	form = forms.TaskForm(instance=task)

	if (request.method == 'POST'):
		form = forms.TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request, 'task_edit.html', {'form': form})


def delete(request, id):
	task = Task.objects.get(id=id)
	task.delete()
	return redirect('home')
