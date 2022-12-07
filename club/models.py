from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=35)
    description = models.TextField
    quantity = models.IntegerField


class Court(models.Model):
    court_types = [(1, 'grass'), (2, 'clay'), (3, 'hard')]
    type = models.IntegerField(choices=court_types)
    court_preference = [(1, 'inside'), (2, 'outside')]
    preference = models.IntegerField(choices=court_types, default=1)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)


class PriceList(models.Model):
    weekdays = models.IntegerField
    weekend = models.IntegerField
