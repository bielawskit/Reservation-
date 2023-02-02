from django import forms
from . import models
from .models import Reservation


# class ReservationForm(forms.ModelForm):
#     # start = forms.DateField(label='Data_start', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     # start = forms.DateTimeField(label='Początek')
#     start = forms.DateTimeField(label='Początek')
#     finish = forms.DateTimeField(label='Koniec')
#
#     class Meta:
#         model = models.Reservation
#         fields = ('start', 'finish', 'coach', 'club')


class DateTimeInput(forms.DateTimeInput):
    input_type = ('datetime-local')


class ExampleForm(forms.Form):
    my_date_time_field = forms.DateTimeField(widget=DateTimeInput)


class ReservationForm(forms.ModelForm):
    start = forms.DateTimeField
    finish = forms.DateTimeField

    class Meta:
        model = models.Reservation
        widgets = {'start': DateTimeInput(),
                   'finish': DateTimeInput()}
        fields = ('start', 'finish', 'coach', 'club')
