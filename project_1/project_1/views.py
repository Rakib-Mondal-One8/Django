from django.http import HttpResponse


def contact(request):
    return HttpResponse('This is contact Page')


def home(request):
    return HttpResponse("This is home Page")
