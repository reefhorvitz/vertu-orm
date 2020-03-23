from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country}'


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=200, null=True, blank=True)
    address_two = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.address_one}, {self.city}'


class Image(models.Model):
    url = models.CharField('Image url', max_length=200)
