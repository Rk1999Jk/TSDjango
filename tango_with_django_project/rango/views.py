#from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
#from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!")
