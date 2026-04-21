from django import forms
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm
from .models import Profile

class RegisterForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','name','email']


class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField()
    class Meta:
        model = User
        fields = ["name", "email","image"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "image": forms.EmailInput(attrs={"class": "form-control"}),
        }
