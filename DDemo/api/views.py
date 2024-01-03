from django.shortcuts import render, HttpResponse
from .models import *
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
    print("jhgfdfg")
    return HttpResponse("kkjhgg")

def indexx(request):
    val = Module.objects.create(first_name="ARIT", last_name="ROY", email = "examplale@gmail.com",
                                phone="1234567")
    return HttpResponse("kkjhgg")

def sum(request):
    print(12+12)
    return HttpResponse(10+20)

