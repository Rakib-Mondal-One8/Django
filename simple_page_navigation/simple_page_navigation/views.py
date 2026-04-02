from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def amd(request):
    return render(request,'amd.html')