from django.shortcuts import render,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return HttpResponse('Hi this is brand')
