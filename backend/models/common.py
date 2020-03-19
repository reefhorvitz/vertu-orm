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
    street = models.CharField(max_length=200)
    number = models.IntegerField('House Number')

    def __str__(self):
        return f'{self.street} {self.number}, {self.city}'
