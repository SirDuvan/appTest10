from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("::::: Estas en el archivo index :::::")

def hello(request):
    return HttpResponse("::::: Este es otro mensaje :::::")

def list_Clients(request):
    return HttpResponse("::::: Aqui se muestra los clientes en la DB :::::")