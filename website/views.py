from django.http import HttpResponse
from django.shortcuts import render

def http_test(request):
    return HttpResponse("HI")


# Create your views here.
