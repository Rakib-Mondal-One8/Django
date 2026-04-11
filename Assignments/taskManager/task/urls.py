from django.urls import path
from . import views

urlpatterns = [
	path('', views.add, name='task_add'),
	path('edit/<int:id>', views.edit, name='task_edit'),
	path('delete/<int:id>', views.delete, name='task_delete'),
]
