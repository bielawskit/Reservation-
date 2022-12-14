from users.models import CustomUser
from django.db import models
from club.models import Club, Coach


class Reservation(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    finish_date = models.DateField()
    finish_time = models.TimeField()

    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user}, {self.club}'
