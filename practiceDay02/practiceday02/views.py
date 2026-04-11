from django.shortcuts import render, redirect

from album.models import Album
from musician.models import Musician


def home(request):
	albums = Album.objects.select_related('musician').all()
	return render(request, 'home.html', {'albums': albums})


def delete(request, musician_id, album_id):
	musician = Musician.objects.get(id=musician_id)
	album = Album.objects.get(id=album_id)

	musician.delete()
	album.delete()

	return redirect('home')
