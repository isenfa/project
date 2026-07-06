from django.shortcuts import render , HttpResponse

def index(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")