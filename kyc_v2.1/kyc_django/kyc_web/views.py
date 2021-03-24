from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "kyc_web/index.html")

def addkyc(request):
    return HttpResponse("<h2> you can add kyc</h2>")