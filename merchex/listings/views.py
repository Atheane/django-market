# listings/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail

def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/band-list.html", { "bands": bands })

def band_detail(request, id):
    band = Band.objects.get(id=id)
    listing = Listing.objects.filter(band=id)
    return render(request, "listings/band-detail.html", { "band": band, "listing": listing })

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band-create.html',
            {'form': form})
    
def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
            'listings/band-update.html',
            {'form': form})
    
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", { "listings": listings })

def listing_band(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/listing-band.html", { "band": band })

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listing-detail.html", { "listing": listing })

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de crtéer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request,
            'listings/listing-create.html',
            { 'form': form })

def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request,
            'listings/listing-update.html',
            {'form': form})

def about_us(request):
    return render(request, "listings/about-us.html")

def contact(request):
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