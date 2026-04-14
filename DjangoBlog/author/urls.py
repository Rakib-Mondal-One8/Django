from django.urls import path,include
from . import views
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    # path("login/", views.user_login, name="login"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    # path("logout/", views.user_logout, name="logout"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit/", views.edit, name="edit"),
    path("passchange/", views.pass_change, name="passchange"),
]
