from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='album_index'),
	path('edit/<int:id>/', views.EditAlbumView.as_view(), name='album_edit'),
]
