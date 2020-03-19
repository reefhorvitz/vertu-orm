from django.db import models


class Heating(models.Model):
    name = models.CharField('Property Heating data', max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField('Property Type', max_length=100)

    def __str__(self):
        return self.name


class Cooling(models.Model):
    name = models.CharField('Property cooling data', max_length=100)

    def __str__(self):
        return self.name


class Parking(models.Model):
    name = models.CharField('Property parking data', max_length=100)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField('Property Facilities', max_length=100)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField('Property Amenity', max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Property Tags', max_length=100)

    def __str__(self):
        return self.name


class OtherData(models.Model):
    name = models.CharField('Propertys Other Data', max_length=100)

    def __str__(self):
        return self.name
