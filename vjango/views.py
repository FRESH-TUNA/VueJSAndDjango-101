from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, "index.html", {'days' : [1, 2, 3]})

def index(request):
    return render(request, "index.html", {'days' : [1, 2, 3]})

def indexTest(request):
    return JsonResponse({'days' : [1, 2, 3]})