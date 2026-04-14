from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from post.models import Post
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = forms.RegisterForm()

    return render(request, "authentication.html", {"form": form,'type':'Signup'})


# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect("profile")
#     if request.method == "POST":
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=name, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Logged In successfully!")
#                 return redirect("profile")
#             else:
#                 messages.warning(request, "User is not registered!")
#                 return redirect("signup")
#     else:
#         form = AuthenticationForm(request=request)

#     return render(request, "login.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "authentication.html"

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Login Information!!")
        response = super().form_invalid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request, "Logged out successfully!")
#     return redirect("login")


@method_decorator(login_required, name = 'dispatch')
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    # print(data.author.name)
    return render(request, "profile.html", {"data": data})


@login_required
def edit(request):
    if request.method == "POST":
        form = forms.UpdateUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!!")
            return redirect("profile")
    else:
        form = forms.UpdateUserData(instance=request.user)

    return render(request, "profile_edit.html", {"form": form})


@login_required
def pass_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password Changed Successfully !!")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "passchange.html", {"form": form})
