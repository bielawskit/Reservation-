from django import forms

from club.models import Coach
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
    class Meta:
        model = Reservation
        widgets = {'start': DateTimeInput(),
                   'finish': DateTimeInput()}
        fields = ('start', 'finish', 'club', 'coach')


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        widgets = {'start': DateTimeInput(),
                   'finish': DateTimeInput()}
        fields = ('start', 'finish', 'club', 'coach')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coach'].queryset = Coach.objects.none()

        if 'club' in self.data:
            try:
                club_id = int(self.data.get('club'))
                self.fields['coach'].queryset = Coach.objects.filter(club_id=club_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty coach queryset
        elif self.instance.pk:
            self.fields['coach'].queryset = self.instance.club.coach_set.order_by('name')
