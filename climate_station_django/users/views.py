from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    response="<h1>hello world</h1>"
    return HttpResponse(response)