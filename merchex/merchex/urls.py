"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about-us/", views.about_us),
    path("contact/", views.contact, name="contact"),
    path("email-sent/", views.email_sent, name="email-sent"),
    # Band
    path("bands/", views.bands, name="bands"),
    path("bands/add/", views.band_create, name="band-create"),
    path("bands/<int:id>/", views.band_detail, name="band-detail"),
    path("bands/<int:id>/change", views.band_update, name="band-change"),
    path("bands/<int:id>/delete", views.band_delete, name="band-delete"),
    # Listing
    path("listings/", views.listings, name="listings"),
    path("listings/add/", views.listing_create, name="listing-create"),
    path("listings/<int:id>/", views.listing_detail, name="listing-detail"),
    path("listing-band/<int:id>/", views.listing_band, name="listing-band"),
    path("listings/<int:id>/change", views.listing_update, name="listing-change"),
    path("listings/<int:id>/delete", views.listing_delete, name="listing-delete"),
]
