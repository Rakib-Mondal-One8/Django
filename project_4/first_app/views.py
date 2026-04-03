from django.shortcuts import render

# Create your views here.
def index(request):
    d = {
        'users': [
            {
                'id':1,
                'first':'Mark',
                'last':'Otto',
                'handle':'@mdo'
            },
            {
                'id': 2,
                'first': 'Jacob',
                'last': 'Thornton',
                'handle': '@fat'
            },
            {
                'id': 3,
                'first': 'John',
                'last': 'Doe',
                'handle': '@social'
            },
            {
                'id': 4,
                'first': 'Anika',
                'last': 'Fatima',
                'handle': '@Babu'
            },
            {
                'id': 5,
                'first': 'Rakib',
                'last': 'Islam',
                'handle': '@18'
            }
        ]
    }
    return render(request,'index.html',d)

def about(request):
    print(request.GET)
    return render(request,'index.html',{'id':request.GET})