from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . import forms
from .models import Musician


# Create your views here.
def index(request):
	if (request.method == 'POST'):
		form = forms.MusicianForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect('home')
	form = forms.MusicianForm()
	return render(request, 'musician_index.html', {'form': form})


def edit(request, id):
	musician = Musician.objects.get(id=id)
	form = forms.MusicianForm(instance=musician)

	if (request.method == 'POST'):
		form = forms.MusicianForm(request.POST, instance=musician)
		if (form.is_valid()):
			form.save()
			return redirect('home')
	return render(request, 'musician_edit.html', {'form': form})
