from django import forms
from django.contrib.auth.forms import UserCreationForm,User,UserChangeForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',required=True)
    last_name = forms.CharField(label='Last Name',required=True)
    email = forms.EmailField(label='Email',required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']