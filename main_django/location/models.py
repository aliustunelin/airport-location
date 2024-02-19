from django.db import models
from django.db.models.functions import Lower
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import Q


#city arguman search
class LocationQuerySet(models.QuerySet):
    def search(self, query):
        unaccent_query = SearchQuery(query, config='turkish_unaccent')

        results = self.annotate(rank=SearchRank(models.functions.Lower('name'), unaccent_query)).filter(
            models.Q(name__iexact=query) |
            models.Q(name__icontains=query)
        ).order_by('-rank')

        return results

class LocationManager(models.Manager):
    def get_queryset(self):
        return LocationQuerySet(self.model, using=self._db).all()

    def search(self, query):
        return self.get_queryset().search(query)





class Country(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    search_text = models.CharField(max_length=100, null=False, blank=False)
    search_count = models.IntegerField(default=0, null=False, blank=False)
    code = models.CharField(max_length=3)
    phone_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    search_text = models.CharField(max_length=100, null=False, blank=False)
    search_count = models.IntegerField(default=0, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    search_text = models.CharField(max_length=100, null=False, blank=False)
    search_count = models.IntegerField(default=0, null=False, blank=False)
    code = models.CharField(max_length=3)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='airports')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    def __str__(self):
        return self.name
    

