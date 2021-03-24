from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h2>hello....... first one</h2>")

def addkyc(request):
    return HttpResponse("<h2> you can add kyc</h2>")