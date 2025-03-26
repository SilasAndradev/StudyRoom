from django.shortcuts import render

rooms = [
    {'id':1,'name':'Vamos aprender Python!'},
    {'id':2,'name':'Vamos aprender Django!'},
    {'id':3,'name':'Vamos aprender Django Rest FrameWork!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html', {'rooms': rooms})
