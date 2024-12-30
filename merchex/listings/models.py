from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        ELECTRONIC = 'E'
        HOUSE = 'H'
        DEEP_HOUSE = 'DH'
        MINIMAL_TECH = 'MT'
        TECHNO = 'T'
        CLASSIC = 'C'
        PROGRESSIVE_ELECTRONIC = 'PE'
        INDIE_ROCK = 'IR'
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=10)
    genre = models.fields.CharField(choices=Genre.choices, default=Genre.HIP_HOP, max_length=2, verbose_name="Genre")
    biography = models.fields.CharField(default='', max_length=1000)
    year_formed = models.fields.IntegerField(
        default=2000,
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)    
    
class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISCELLANEOUS = 'M'
    def __str__(self):
        return f'{self.title}'
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.fields.CharField(choices=Type.choices, default=Type.RECORDS, max_length=2, verbose_name="Type")