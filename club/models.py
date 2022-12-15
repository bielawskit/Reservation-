from django.contrib.auth import get_user_model
from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=35)
    quantity = models.IntegerField(null=False)
    type = [(1, 'Akceptuje'), (2, 'Nie akceptuje')]
    multisport = models.IntegerField(choices=type)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Court(models.Model):
    name = models.CharField(max_length=20)
    court_types = [(1, 'grass'), (2, 'clay'), (3, 'hard')]
    type = models.IntegerField(choices=court_types)
    court_preference = [(1, 'inside'), (2, 'outside')]
    preference = models.IntegerField(choices=court_preference)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PriceList(models.Model):
    cost = models.IntegerField()
    court = models.ForeignKey('Court', on_delete=models.DO_NOTHING)

    def __str__(self):
        return {self.cost}


class Coach(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    price = models.IntegerField()
    club = models.ForeignKey('Club', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
