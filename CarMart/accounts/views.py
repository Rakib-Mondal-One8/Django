from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from car.models import Order
from .models import Profile


# Create your views here.


class SignupView(CreateView):
    form_class = forms.RegisterForm
    template_name = "authentication.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "User Registered Successfully !!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Signup"
        return context


class UserLoginView(LoginView):
    template_name = "authentication.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged-In Successfully!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Login Information !!")
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


class ProfileView(LoginRequiredMixin, ListView):
    template_name = "profile.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model: User
    template_name = "profile_edit.html"
    form_class = forms.ProfileEditForm
    success_url = reverse_lazy("profile")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES,instance=self.object)

        if form.is_valid() and request.user.is_authenticated:
            user = form.save()

            profile, created = Profile.objects.get_or_create(user=user)
            if request.FILES.get("image"):
                profile.image = request.FILES["image"]
                profile.save()

                return redirect(self.success_url)

        return self.form_invalid(form)

    def get_object(self):
        return self.request.user


class UserLogoutView(LoginRequiredMixin,LogoutView):
    next_page = reverse_lazy("home")
