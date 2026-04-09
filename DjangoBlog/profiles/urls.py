from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path('add/',views.add_profile,name='add_profile')
]
