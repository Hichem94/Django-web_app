from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


def listings(request):
    return HttpResponse('<h1>On va lister les annonces pour les articles</h1>')


def contact(request):
    return HttpResponse('<h1>Contacter nous à l\'adresse merchex@gmail.com </h1>')

