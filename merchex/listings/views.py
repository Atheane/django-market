from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/bands.html", {"bands": bands })
    
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": listings })
    
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about_us(request):
    return HttpResponse('<h1>About us</h1>')

def help(request):
    return HttpResponse('<h1>Help</h1><p>Please contact us at contact@merchex.com</p>')