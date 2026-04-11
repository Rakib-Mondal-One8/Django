from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index),
    path('page2/',views.page2)
]
