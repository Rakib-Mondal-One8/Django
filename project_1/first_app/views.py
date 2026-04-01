from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is the first_app page!!')

def courses(request):
    return HttpResponse('THis is Courses page!!')

def about(request):
    return HttpResponse('This is the about page!!')