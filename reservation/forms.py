from django import forms
import datetime
from club.models import Coach, Court

from .models import Reservation


class DateTimeInput(forms.DateTimeInput):
    input_type = ('datetime-local')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        widgets = {'start': DateTimeInput(),
                   'finish': DateTimeInput()}
        fields = ('start', 'finish', 'club', 'court', 'coach')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coach'].queryset = Coach.objects.none()
        self.fields['court'].queryset = Court.objects.none()

        if 'club' in self.data:
            try:
                club_id = int(self.data.get('club'))
                self.fields['coach'].queryset = Coach.objects.filter(club_id=club_id).order_by('name')
                self.fields['court'].queryset = Court.objects.filter(club_id=club_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty coach queryset
        elif self.instance.pk:
            self.fields['coach'].queryset = self.instance.club.coach_set.order_by('name')
            self.fields['court'].queryset = self.instance.club.court_set.order_by('name')

