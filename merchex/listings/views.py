from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>Hello Django !</h1>
                        <p>Mes groupes préférés sont :<p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                        </ul>                   
                        """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


def listings(request):
    l = Listing.objects.all()
    return HttpResponse(f"""<h1>On va lister les annonces pour les articles : </h1>
                        <ul>
                            <li>{l[0].title}</li>
                            <li>{l[1].title}</li>
                            <li>{l[2].title}</li>
                            <li>{l[3].title}</li>
                        </ul>  
                        """)


def contact(request):
    return HttpResponse('<h1>Contacter nous à l\'adresse merchex@gmail.com </h1>')

