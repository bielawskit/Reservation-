from django import forms
from django.core.exceptions import ValidationError

from . import models
from .models import Club


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = ('name', 'location', 'quantity', 'multisport')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     name2 = Club.objects.get('name')
    #     if name == name2:
    #         raise ValidationError('Klub o podanej nazwie istnieje.')
    #     return name
    #
    # def save(self, commit=True):
    #     club = super().save(commit=False)
    #     club.set_name(self.cleaned_data.get('name'))
    #
    #     if commit:
    #         club.save()
    #
    #     return club

    # def clean_location(self):
    #     location = self.cleaned_data.get('location')
    #
    #     if location == location:
    #         raise ValidationError('Pod tym adresem znajduje się już klub.')
    #     return location


class CourtForm(forms.ModelForm):
    class Meta:
        model = models.Court

        fields = ('club', 'name', 'type', 'preference')


class CoachForm(forms.ModelForm):
    class Meta:
        model = models.Coach

        fields = ('club', 'name', 'surname', 'price')


class ClubFormSEdit(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = ('name', 'location', 'quantity', 'multisport')


class CoachFormEdit(forms.ModelForm):
    class Meta:
        model = models.Coach
        fields = ('name', 'surname', 'price', 'club')


class PriceListForm(forms.ModelForm):
    class Meta:
        model = models.PriceList

        fields = ('court', 'cost')
