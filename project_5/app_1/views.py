from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")

        return render(request, "about.html", {"name": name, "email": email})
    return render(request, "about.html")


def submit_form(request):

    return render(request, "form.html")


def django_form(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data["file"]
            # with open('./app_1/upload/' + file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = forms.ContactForm()

    return render(request, "django_form.html", {"form": form})


def student_form(request):
    if(request.method == 'POST'):
        form = forms.StudentForm(request.POST,request.FILES)
        if(form.is_valid()):
            print(form.cleaned_data)
    else:
        form = forms.StudentForm()
    
    return render(request,'django_form.html',{'form':form})

def password_validation_form(request):
    if(request.method == 'POST'):
        form = forms.PasswordValidation(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
    else: 
        form = forms.PasswordValidation()

    return render(request,'django_form.html',{'form':form})