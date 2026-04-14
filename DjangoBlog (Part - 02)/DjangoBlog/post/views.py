from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if(request.method == 'POST'):
        form = forms.PostForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("add_post")
    else:
        form = forms.PostForm()    
    return render(request, 'post_add.html',{'form':form})

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    
    if(request.method == 'POST'):
        form = forms.PostForm(request.POST,instance=post)
        if(form.is_valid()):
            # form.instance.author = request.user
            form.save()
            return redirect('profile')
    else:
        form = forms.PostForm(instance=post)
    return render(request,'post_edit.html',{'form':form})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('profile')
