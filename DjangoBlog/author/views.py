from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def index(request):
    
    form = forms.AuthorForm()
    return render(request,'author_index.html',{'form':form})

def add_author(request):
    if(request.method == 'POST'):
        form = forms.AuthorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('author_index')