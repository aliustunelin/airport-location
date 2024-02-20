from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Airport, City, Country
from .serializers import CitySerializers, CountrySerializers, AirportSerializers

# Create your views here.

class CreateCountry(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers