from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    SetPasswordForm,
    PasswordChangeForm,
)
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created successfully!")
            form.save()
            return redirect("login")
    else:
        form = forms.RegisterForm()
    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                return redirect("signup")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.UpdateUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Profile Successfully Updated!!')
        else:
            form = forms.UpdateUserData(instance=request.user)
        return render(request, "profile.html", {"form": form})
    else:
        return redirect("login")


def pass_change(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "passchange.html", {"form": form})


def pass_change2(request):

    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "passchange.html", {"form": form})


