#   load_initial_data.py
import json
from django.core.management.base import BaseCommand
from location.models import Country
from django.apps import apps

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **options):
        try:
            with open('fixtures/countries.json', 'r') as file:
                data = json.load(file)

            for entry in data:
                model_name = 'location.Country'
                model = apps.get_model(model_name)
                
                text = entry['name']
                data_dict = {'name': text}
                
                
                instance = self.country_load(model_name, model, data_dict)
                
        except:
            self.stdout.write(self.style.ERROR_OUTPUT(f'Failed created {model_name} instance with pk {instance.pk}'))
            

            

    def country_load(self, model_name, model, data_dict):
        instance = model.objects.create(**data_dict)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {model_name} instance with pk {instance.pk}'))
        return instance
        
            
    
    