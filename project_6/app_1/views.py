from django.shortcuts import render
from django.shortcuts import redirect
from . import models
# Create your views here.
def home(request):
    data = models.Student.objects.all()
    # data = models.Teacher.objects.all()

    return render(request,'home.html',{'data':data})


def delete_student(request,roll):
    student = models.Student.objects.filter(roll=roll)
    student.delete()

    return redirect('home')