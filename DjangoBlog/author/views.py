from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from post.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        form = forms.RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = forms.RegisterForm()

    return render(request,'signup.html',{'form':form})


def user_login(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(request=request,data=request.POST)
        if(form.is_valid()):
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=name,password=password)

            if user is not None:
                login(request,user)
                messages.success(request, "Logged In successfully!")
                return redirect('profile')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm(request=request)

    return render(request,'login.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    # print(data.author.name)
    return render(request,'profile.html',{'data':data})

@login_required
def edit(request):
    if(request.method == 'POST'):
        form = forms.UpdateUserData(request.POST,instance=request.user)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Profile Updated Successfully!!")
            return redirect('profile')
    else:
        form = forms.UpdateUserData(instance=request.user)

    return render(request,'profile_edit.html',{'form':form})

@login_required
def pass_change(request):
    if(request.method == 'POST'):
        form = PasswordChangeForm(user=request.user ,data=request.POST)
        if(form.is_valid()):
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,'Password Changed Successfully !!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})
