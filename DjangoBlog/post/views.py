from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def index(request):
    form = forms.PostForm()    
    return render(request, 'post_index.html',{'form':form})

def add_post(request):
    if(request.method == 'POST'):
        form = forms.PostForm(request.POST)
        if(form.is_valid()):
            print(form)
            form.save()
        else:
            print('THis is not a valid form !')

        return redirect('post_index')
