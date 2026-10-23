from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def greet(request, name=""):
    if name == "":
        return HttpResponse(f"Hello Stranger!")
    
    else:
        return HttpResponse(f"Hello {name}!")
    

