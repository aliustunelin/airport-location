from django.core.management.base import BaseCommand
from ...models import Airport, City, Country
import json
import os


class Command(BaseCommand):
    help = 'Load custom data from JSON file'

    def handle(self, *args, **options):
        json_cities_file_path = 'fixtures/countries.json'

        try:
            if os.path.exists(json_cities_file_path):
                self.stdout.write(self.style.HTTP_INFO('This is true state'))
            else:
                self.stdout.write(self.style.HTTP_INFO(f'Error: File not found at path {json_cities_file_path}'))
            with open(json_cities_file_path, 'r') as json_file:
                self.stdout.write(self.style.HTTP_INFO('now here'))
                data = json.load(json_file)
                
                
                for item in data:
                    Country.objects.create(
                        name=item['name'],
                        
                    )

            self.stdout.write(self.style.SUCCESS('Successfully  cities loaded custom data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading custom data: {str(e)}'))
