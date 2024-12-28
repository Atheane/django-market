from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/bands.html", {"bands": bands })
    
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": listings })

def about_us(request):
    return render(request, "listings/about-us.html")

def help(request):
    return render(request, "listings/help.html")
