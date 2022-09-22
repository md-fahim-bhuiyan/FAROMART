from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'shop/index.html')

def about(request):
   return render(request, 'shop/about.html')

def contact(request):
   return render(request, 'shop/contact/index.html')

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")