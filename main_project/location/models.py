from django.db import models

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
    

