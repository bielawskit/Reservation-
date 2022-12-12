from django import forms
from . import models


class ReservationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    start_time = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'time'}))
    finish_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    finish_time = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'time'}))

    class Meta:
        model = models.Reservation
        fields = ('start_date', 'start_time', 'finish_date', 'finish_time', 'coach', 'club')
