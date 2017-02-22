from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Memius. You are now with Python.")

# Create your views here.
