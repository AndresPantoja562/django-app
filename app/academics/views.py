from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcom to my site")
def list_persons(request):
    return HttpResponse("here you find a list of people")
