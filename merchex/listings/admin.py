from django.contrib import admin

# Register your models here.
from listings.models import Band, Listing

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')  
    
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'sold', "band")  