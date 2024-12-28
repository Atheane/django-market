from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about_us(request):
    return HttpResponse('<h1>About us</h1>')

def help(request):
    return HttpResponse('<h1>Help</h1><p>Please contact us at contact@merchex.com</p>')