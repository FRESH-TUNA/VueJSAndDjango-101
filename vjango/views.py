from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {'days' : [1, 2, 3]})

def index(request):
    return render(request, "index.html", {'days' : [1, 2, 3]})

def indexTest(request):
    return HttpResponse('[1, 2, 3]')