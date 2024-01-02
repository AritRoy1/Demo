from django.shortcuts import render, HttpResponse
from .models import Module
# Create your views here.
def Sum(request):
    return HttpResponse("knki dihdkd h")

def Calculate(request):
    return HttpResponse("calculate")

def Mul(request):
    return HttpResponse("multiplay")
    
def asd(request):
    return HttpResponse("kkjhgg")

def index(request):
    Module.objects.create(first_name = "Arit", last_name="Roy", email="example@gmail.com", phone="12345")
    return HttpResponse("kkjhgg")

