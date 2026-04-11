from django.urls import path
from . import views

urlpatterns = [
	path('',views.add,name='category_add'),
]
