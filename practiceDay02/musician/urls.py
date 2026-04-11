from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='musician_index'),
	path('edit/<int:id>', views.edit, name='musician_edit'),
]
