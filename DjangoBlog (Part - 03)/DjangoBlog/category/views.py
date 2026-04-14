from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def index(request):
    form = forms.CategoryForm()
    return render(request,'category_index.html',{'form':form})

def add_category(request):
    if(request.method == 'POST'):
        form = forms.CategoryForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('category_index')
    # else:
    #     return redirect('category_index')