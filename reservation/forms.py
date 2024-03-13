from club.models import Coach, Court
from .models import Reservation
from django import forms
from django.core.exceptions import ValidationError


class DateTimeInput(forms.DateTimeInput):
    input_type = "text"
    template_name = "reservation/custom_datetime_input.html"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        widgets = {
            "start": DateTimeInput(attrs={"readonly": "readonly"}),
            "finish": DateTimeInput(attrs={"readonly": "readonly"}),
        }
        fields = ("start", "finish", "club", "court", "coach")

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        finish = cleaned_data.get("finish")
        court = cleaned_data.get("court")
        coach = cleaned_data.get("coach")

        if start and finish:
            if start >= finish:
                self.add_error(
                    "finish",
                    "Data zakończenia nie może być wcześniejsza lub równa dacie rozpoczęcia.",
                )

            overlapping_reservations = Reservation.objects.filter(
                court=court, start__lt=finish, finish__gt=start
            ).exists()

            if overlapping_reservations:
                raise ValidationError(
                    "Ten kort jest już zarezerwowany w wybranym terminie."
                )

            if coach:
                overlapping_coach_reservations = Reservation.objects.filter(
                    coach=coach, start__lt=finish, finish__gt=start
                ).exists()

                if overlapping_coach_reservations:
                    self.add_error("coach", "Trener niedostępny w wybranym terminie.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["coach"].queryset = Coach.objects.none()
        self.fields["court"].queryset = Court.objects.none()

        if "club" in self.data:
            try:
                club_id = int(self.data.get("club"))
                self.fields["coach"].queryset = Coach.objects.filter(
                    club_id=club_id
                ).order_by("name")
                self.fields["court"].queryset = Court.objects.filter(
                    club_id=club_id
                ).order_by("name")
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["coach"].queryset = self.instance.club.coach_set.order_by(
                "name"
            )
            self.fields["court"].queryset = self.instance.club.court_set.order_by(
                "name"
            )
