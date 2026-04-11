from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def index(request):
    form = forms.ProfileForm()
    return render(request,'profiles_index.html',{'form':form})

def add_profile(request):
    if(request.method == 'POST'):
        form = forms.ProfileForm(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print('Form is not Valid !!')
        return redirect('profiles_index')