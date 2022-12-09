from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=35)
    quantity = models.IntegerField()
    type = [(1, 'Akceptuje'), (2, 'Nie akceptuje')]
    multisport = models.IntegerField(choices=type)

    def __str__(self):
        return self.name


class Court(models.Model):
    name = models.CharField(max_length=20)
    court_types = [(1, 'grass'), (2, 'clay'), (3, 'hard')]
    type = models.IntegerField(choices=court_types)
    court_preference = [(1, 'inside'), (2, 'outside')]
    preference = models.IntegerField(choices=court_preference, default=1)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PriceList(models.Model):
    court_price = [(70, '6-10'), (60, '10-14'), (80, '14-22')]
    cost = models.IntegerField(choices=court_price)
    court = models.ForeignKey('Court', on_delete=models.CASCADE)
