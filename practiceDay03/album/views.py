from django.shortcuts import render, redirect
from . import forms
from .models import Album

from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView, CreateView


@method_decorator(login_required, name="dispatch")
class IndexView(CreateView):
    model = Album
    form_class = forms.AlbumForm
    template_name = "album_index.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Album Added Successfully!!")
        return super().form_valid(form)


# def edit(request, id):
# 	album = Album.objects.get(id=id)
# 	form = forms.AlbumForm(instance=album)
# 	if (request.method == 'POST'):
# 		form = forms.AlbumForm(request.POST, instance=album)
# 		if (form.is_valid()):
# 			form.save()
# 			return redirect('home')

# 	return render(request, 'album_edit.html', {'form': form})

@method_decorator(login_required,name='dispatch')
class EditAlbumView(UpdateView):
	model = Album
	form_class = forms.AlbumForm
	success_url = reverse_lazy('home')
	template_name = 'album_edit.html'
	pk_url_kwarg = 'id'

	def form_valid(self, form):
		messages.success(self.request,'Album Edited Successfully!!')
		return super().form_valid(form)
	
	def form_invalid(self, form):
		print(form.errors)
		return super().form_invalid(form)
