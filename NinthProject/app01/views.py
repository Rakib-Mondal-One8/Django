from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
# def home(request):
#     response = render(request,'home.html')
#     # response.set_cookie('name','rakib',max_age=60*3)
#     response.set_cookie("name", "rakib", expires=datetime.utcnow()+timedelta(days=7))
#     return response

def home(request):
    data = {
        'name':'rakib',
        'age':20
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request,'home.html')

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'home.html',{'name':name})

def delete_cookie(request):
    response = render(request,'delete_cookie.html')
    response.delete_cookie('name')
    return response

def get_session(request):
    name = request.session.get('name')
    age = request.session.get('age')

    return render(request,'home.html',{'name':name,'age':age})

def delete_session(request):

    request.session.flush()
    return render(request,'delete_session.html')
