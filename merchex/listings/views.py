from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing, Contact

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands':bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    l = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings':l})


def contact(request):
    contact = Contact.objects.all()
    return render(request, 'listings/contact.html', {'contact':contact})


