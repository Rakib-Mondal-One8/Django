from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,User,UserChangeForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UpdateUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
