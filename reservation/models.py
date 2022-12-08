from users.models import CustomUser
from django.db import models
from club.models import Club


class Coach(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()

    coach = models.ForeignKey('Coach', on_delete=models.DO_NOTHING)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user}, {self.club}, {self.start} - {self.finish}'
