from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='album_index'),
	path('edit/<int:id>', views.edit, name='album_edit'),
]
