from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing, Contact
from django.shortcuts import get_object_or_404

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/band_list.html', 
                  {'bands':bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
   #band = Band.objects.get(id=id)
   band = get_object_or_404(Band, id=id)
   return render(request,
          'listings/band_detail.html',
         {'band':band}) # nous passons l'id au modèle


def about(request):
    return render(request, 'listings/about.html')


def listings_list(request):
    l = Listing.objects.all()
    return render(request, 'listings/listings_list.html', {'listings':l})

def listings_detail(request, id):
    #l = Listing.get_objects.get(id=id)
    l = get_object_or_404(Listing, id=id)
    band = get_object_or_404(Band, id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'listing':l, 'band':band})

def contact(request):
    contact = Contact.objects.all()
    return render(request, 'listings/contact.html', {'contact':contact})


