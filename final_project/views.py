from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html', context={})

def hello(request):
    return HttpResponse('Hello world!')

def actual_time(request):
    today = datetime.now().date()
    return HttpResponse(f"Today's date is {today}")
#Para cuando pasamos parametros desde el front#
def age_view(request, age):
    return HttpResponse(f'Your age is {age}')

def name(request,name):
    return HttpResponse(f'Your name is {name}')
##
def home(request):
    return render(request, 'home.html', context={})  