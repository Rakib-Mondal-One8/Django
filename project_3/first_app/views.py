import datetime

from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author':'eren','age':15,'arr':['Eren','Yeger','18'],'dt': datetime.datetime.now(), 'courses':[

        {
            'id':1,
            'name' : 'Python',
            'fees' : '1000'
        },
        {
            'id':2,
            'name': 'Django',
            'fees': '2000'
        },
        {
            'id':3,
            'name':'C++',
            'fees':'5000'
        }
    ]}
    return render(request,'home.html',d)