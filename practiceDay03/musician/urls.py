from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='musician_index'),
	path('edit/<int:id>/', views.EditMusicianView.as_view(), name='musician_edit'),
]
