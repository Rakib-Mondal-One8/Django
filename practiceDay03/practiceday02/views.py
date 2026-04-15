from django.shortcuts import render, redirect

from album.models import Album
from musician.models import Musician


from django.views.generic import CreateView, DeleteView,DetailView,ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# def home(request):
#     albums = Album.objects.select_related("musician").all()
#     return render(request, "home.html", {"albums": albums})


class HomeView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'albums'
    
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context[""] = 
	# 	return context
	
    

# def delete(request, musician_id, album_id):
# 	musician = Musician.objects.get(id=musician_id)
# 	album = Album.objects.get(id=album_id)

# 	musician.delete()
# 	album.delete()

# 	return redirect('home')


@method_decorator(login_required, name="dispatch")
class DeleteDataView(DeleteView):
    model = Album
    template_name = "delete.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        album = self.kwargs.get("album_id")
        musician_id = self.kwargs.get("musician_id")

        return get_object_or_404(Album, id=album, musician_id=musician_id)


class SignupView(CreateView):
    form_class = forms.RegisterForm
    template_name = "authentication.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "User is successfully registered!!")
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
        messages.success(self.request, "Logged-In Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Login Information!!")
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


@method_decorator(login_required, name="dispatch")
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")
