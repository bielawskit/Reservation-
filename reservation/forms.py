from django import forms
from . import models


class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ('start', 'finish', 'coach', 'club')
