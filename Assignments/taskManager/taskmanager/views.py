from django.shortcuts import render

from category.models import Category
from task.models import Task


def home(request):
	tasks = Task.objects.prefetch_related('category').all()
	return render(request,'home.html',{'tasks':tasks})