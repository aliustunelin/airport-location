from django.contrib import admin
from location.models import Country, City, Airport
# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)