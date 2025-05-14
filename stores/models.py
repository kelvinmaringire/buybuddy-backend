from django.db import models

from django.contrib.gis.db import models as postgis_models
from django.utils.translation import gettext as _

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from wagtailgeowidget import geocoders
from wagtailgeowidget.panels import GeoAddressPanel, GoogleMapsPanel

from accounts.models import CustomUser


@register_snippet
class Store(index.Indexed, models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = postgis_models.PointField(geography=True, srid=4326, null=True, blank=True)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("phone_number"),
        FieldPanel("website"),
        MultiFieldPanel([
            GeoAddressPanel("address", geocoder=geocoders.GOOGLE_MAPS),
            GoogleMapsPanel('location', address_field='address'),
        ], _('Geo details')),
    ]

    search_fields = [
        index.SearchField('name'),
        index.SearchField('address'),
    ]


@register_snippet
class Deal(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(max_length=150)
    description = models.TextField()
    pic = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_query_name='deal_pic')
    start_date = models.DateField()
    end_date = models.DateField()
    terms_and_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.store.name}"

    panels = [
        FieldPanel("store"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("pic"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("terms_and_conditions"),
    ]


@register_snippet
class ShoppingList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='shopping_lists')
    deals = models.ManyToManyField(Deal, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Shopping List"

    panels = [
        FieldPanel("user"),
        FieldPanel("deals"),
    ]


