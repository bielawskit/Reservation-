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
    court_types = [(1, 'Sztuczna trawa'), (2, 'Mączka'), (3, 'Beton')]
    type = models.IntegerField(choices=court_types)
    court_preference = [(1, 'wewnętrzny'), (2, 'zewnętrzny')]
    preference = models.IntegerField(choices=court_preference)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.name}, Cena: {self.cost}"


class Coach(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    price = models.IntegerField()
    club = models.ForeignKey('Club', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
