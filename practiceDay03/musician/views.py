from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . import forms
from .models import Musician

from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DetailView, FormView, CreateView


# Create your views here.
# def index(request):
# 	if (request.method == 'POST'):
# 		form = forms.MusicianForm(request.POST)
# 		if (form.is_valid()):
# 			form.save()
# 			return redirect('home')
# 	form = forms.MusicianForm()
# 	return render(request, 'musician_index.html', {'form': form})

@method_decorator(login_required,name='dispatch')
class IndexView(CreateView):
	model = Musician
	form_class = forms.MusicianForm
	template_name = 'musician_index.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		messages.success(self.request,'Musician Added Successfully!!')
		return super().form_valid(form)


# def edit(request, id):
# 	musician = Musician.objects.get(id=id)
# 	form = forms.MusicianForm(instance=musician)

# 	if (request.method == 'POST'):
# 		form = forms.MusicianForm(request.POST, instance=musician)
# 		if (form.is_valid()):
# 			form.save()
# 			return redirect('home')
# 	return render(request, 'musician_edit.html', {'form': form})

@method_decorator(login_required,name='dispatch')
class EditMusicianView(UpdateView):
	model = Musician
	form_class = forms.MusicianForm
	success_url = reverse_lazy('home')
	template_name = 'musician_edit.html'
	pk_url_kwarg = 'id'

	def form_valid(self, form):
		messages.success(self.request,'Musician Updated Successfully !!')
		return super().form_valid(form)
