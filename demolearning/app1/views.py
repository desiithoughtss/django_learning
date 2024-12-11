from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

def hello(request):
    return HttpResponse("hello world")

def returnHtml(request):
    return HttpResponse("<h1>Hello World</h1>")

def dynamicUrl(request, id):
    return HttpResponse(f"this is the dynamic URL {id}")

def comingHere(request):
    return HttpResponse("this link uses the the include function")

def anotherHere(request, id):
    if id <= 5:
        return HttpResponse(f"this is the another URL {id}")
    else:
        return HttpResponseNotFound("this is the another url, and the id is greater than 5")

def redirecting(request):
    return HttpResponseRedirect("https://www.google.com")


def newRedirect(request, id):
    return HttpResponseRedirect(f"/dynamicUrl/{id}")