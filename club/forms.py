from django import forms
from . import models


class ClubForm(forms.ModelForm):
    class Meta:
        model = models.Club
        fields = ('name', 'location')
