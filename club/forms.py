from django import forms
from django.core.exceptions import ValidationError

from club.models import Club, Coach, Court


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ("name", "location", "quantity", "multisport")

        labels = {
            "name": "Nazwa",
            "location": "Lokalizacja",
            "quantity": "Ilość kortów",
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        location = cleaned_data.get("location")

        if Club.objects.filter(name=name).exists():
            self.add_error("name", "Klub o tej nazwie już istnieje.")

        if Club.objects.filter(location=location).exists():
            self.add_error("location", "Klub w tej lokalizacji już istnieje.")

        return cleaned_data


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court

        fields = ("club", "name", "type", "preference", "cost")

        labels = {
            "club": "Klub",
            "name": "Nazwa",
            "type": "Rodzaj nawierzchni",
            "preference": "Wewnętrzny/Zewnętrzny",
            "cost": "Cena",
        }


class CourtFormEdit(forms.ModelForm):
    class Meta:
        model = Court
        fields = ("club", "name", "type", "preference", "cost")


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach

        fields = ("club", "name", "surname", "price")

        labels = {
            "club": "Klub",
            "name": "Imie",
            "surname": "Nazwisko",
            "price": "Stawka godzinowa",
        }


class ClubFormEdit(forms.ModelForm):
    class Meta:
        model = Club
        fields = ("name", "location", "quantity", "multisport")

        labels = {
            "name": "Nazwa",
            "location": "Lokalizacja",
            "quantity": "Ilość kortów",
            "multisport": "Multisport",
        }


class CoachFormEdit(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ("name", "surname", "price", "club")

        labels = {
            "club": "Klub",
            "name": "Imie",
            "surname": "Nazwisko",
            "price": "Stawka godzinowa",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CoachFormEdit, self).__init__(*args, **kwargs)

        if user:
            self.fields["club"].queryset = Club.objects.filter(user=user)
