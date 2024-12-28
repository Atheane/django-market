from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def bands_list(request):
    bands = Band.objects.all()
    li = ''.join(f"<li>{band.name}</li>" for band in bands)
    return HttpResponse(f"""
            <h1>Hello Django !</h1>
            <p>Mes groupes préférés sont :<p>
            <ul>
                {li}
            </ul>
    """)
    
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about_us(request):
    return HttpResponse('<h1>About us</h1>')

def help(request):
    return HttpResponse('<h1>Help</h1><p>Please contact us at contact@merchex.com</p>')