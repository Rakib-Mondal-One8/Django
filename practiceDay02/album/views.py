from django.shortcuts import render, redirect
from . import forms
from .models import Album


def index(request):
	if (request.method == 'POST'):
		form = forms.AlbumForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect('home')
	form = forms.AlbumForm()
	return render(request, 'album_index.html', {'form': form})


def edit(request, id):
	album = Album.objects.get(id=id)
	form = forms.AlbumForm(instance=album)
	if (request.method == 'POST'):
		form = forms.AlbumForm(request.POST, instance=album)
		if (form.is_valid()):
			form.save()
			return redirect('home')

	return render(request, 'album_edit.html', {'form': form})
