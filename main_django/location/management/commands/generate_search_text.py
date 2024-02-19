
from django.core.management.base import BaseCommand
from location.models import Airport, City, Country

class Command(BaseCommand):
    help = 'Generates search_text for all Location models'

    def handle(self, *args, **options):
        airports = Airport.objects.all()
        for airport in airports:
            search_text = f"{airport.name},{airport.city.name},{airport.country.name}"
            airport.search_text = search_text
            airport.save()

        cities = City.objects.all()
        for city in cities:
            search_text = f"{city.name},{city.country.name}"
            city.search_text = search_text
            city.save()

        countries = Country.objects.all()
        for country in countries:
            search_text = f"{country.name}"
            country.search_text = search_text
            country.save()

        self.stdout.write(self.style.SUCCESS('Search text generation completed successfully.'))
