from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/band-list.html", { "bands": bands })

def band_detail(request, id):
    band = Band.objects.get(id=id)
    listing = Listing.objects.filter(band=id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>", listing)
    return render(request, "listings/band-detail.html", { "band": band, "listing": listing })
    
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", { "listings": listings })

def listing_band(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/listing-band.html", { "band": band })

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listing-detail.html", { "listing": listing })

def about_us(request):
    return render(request, "listings/about-us.html")

def help(request):
    return render(request, "listings/help.html")
