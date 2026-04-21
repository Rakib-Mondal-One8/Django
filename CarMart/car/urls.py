from django.urls import path, include
from . import views

urlpatterns = [
    path("details/<int:pk>/",views.CarDetailView.as_view() , name='car_details'),
    path("order/<int:pk>/",views.order,name='order'),
]
