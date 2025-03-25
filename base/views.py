from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Página principal</h1>')

def room(request):
    return HttpResponse('<h1>Salas</h1>')
 
