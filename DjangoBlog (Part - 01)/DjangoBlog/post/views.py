from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def index(request):
    form = forms.PostForm()    
    return render(request, 'post_index.html',{'form':form})

def add_post(request):
    if(request.method == 'POST'):
        form = forms.PostForm(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            print('THis is not a valid form !')

        return redirect('post_index')


def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    
    if(request.method == 'POST'):
        form = forms.PostForm(request.POST,instance=post)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    else:
        form = forms.PostForm(instance=post)
    return render(request,'post_edit.html',{'form':form})


def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
