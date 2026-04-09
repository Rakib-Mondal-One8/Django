from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='post_index'),
    path('add/',views.add_post,name='add_post')
]
