from rest_framework import serializers
from .models import Country, Airport, City

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def validate_sayfa(self, VAL):
        if VAL <= 1:
            raise serializers.ValidationError("Name Value Upper Then 1.")
        return VAL

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def validate_sayfa(self, VAL):
        if VAL <= 1:
            raise serializers.ValidationError("Name Value Upper Then 1.")
        return VAL


class AirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

    def validate_sayfa(self, VAL):
        if VAL <= 1:
            raise serializers.ValidationError("Name Value Upper Then 1.")
        return VAL
