from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)


class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    country = models.ForeignKey(Country)


class City(models.Model):
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State)


class Day(models.Model):
    date = models.DateTimeField()
    city = models.ForeignKey(City)
    temp = models.IntegerField()

    class Meta:
        unique_together = ('date', 'city')