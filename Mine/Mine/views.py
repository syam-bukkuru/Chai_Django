from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hellow we are in Home page..")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("We are in About page..")
    return render(request, 'about.html')
    

def contact(request):
    #return HttpResponse("We are in Contact page..")
    return render(request, 'contact.html')