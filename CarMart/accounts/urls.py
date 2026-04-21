from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("edit/profile/",views.ProfileEditView.as_view(),name='profile_edit')
]
