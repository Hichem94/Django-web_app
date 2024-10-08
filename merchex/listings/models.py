from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RAP'  
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=([MinValueValidator(1900), MaxValueValidator(2024)])
    )        
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORD   = 'RECORD'
        CLOTHING = 'CLOTHING'
        POSTER   = 'POSTER'
        DIVERS   = 'DIVERS'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=([MinValueValidator(1900), MaxValueValidator(2024)])
    )
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'

class Contact(models.Model):
    mail = models.fields.CharField(max_length=100)