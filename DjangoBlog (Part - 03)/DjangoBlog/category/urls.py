from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='category_index'),
    path('add/',views.add_category,name='add_category')
]
