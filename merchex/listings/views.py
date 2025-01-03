# listings/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail

def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/band-list.html", { "bands": bands })

def band_detail(request, id):
    band = Band.objects.get(id=id)
    listing = Listing.objects.filter(band=id)
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

def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')  # ajoutez cette instruction de retour
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", { "form": form })

def email_sent(request):
    return render(request, "listings/email-sent.html")