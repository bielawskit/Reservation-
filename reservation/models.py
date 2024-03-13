from users.models import CustomUser
from django.db import models
from club.models import Club, Coach, Court


class Reservation(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()

    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    court = models.ForeignKey(Court, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user}, {self.club}, {self.court}, {self.start}, {self.finish}"
