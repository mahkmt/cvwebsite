from django.http import HttpResponse
from django.shortcuts import render

def http_test(request):
    return HttpResponse("*** HI ***")

def index_view(request):
    return HttpResponse("This is homepage of my site.")

def about_view(request):
    return HttpResponse("This is about us...")

def contact_view(request):
    return HttpResponse("This is contact page.")

# Create your views here.
