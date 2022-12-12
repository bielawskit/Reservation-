from django import forms
from . import models


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = ('name', 'location', 'quantity', 'multisport')


class CourtForm(forms.ModelForm):
    class Meta:
        model = models.Court

        fields = ('club', 'name', 'type', 'preference')


class CoachForm(forms.ModelForm):
    class Meta:
        model = models.Coach

        fields = ('club', 'name', 'surname', 'price')


class ClubFormEdit(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = ('name', 'location', 'quantity', 'multisport')
