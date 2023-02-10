import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from club.models import Coach, Court
from reservation.forms import ReservationForm
from reservation.models import Reservation


class ReservationAddView(LoginRequiredMixin, View):
    model = Reservation
    template_name = 'reservation/reservation.html'
    form_class = ReservationForm

    def get(self, request):
        form = self.form_class()
        # form.fields['club'].queryset = models.Club.objects.filter(coach=request.coach)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home:home')
        else:
            return render(request, self.template_name, {'form': form})


def get_coach(request):
    data = json.loads(request.body)
    club_id = data["id"]
    coaches = Coach.objects.filter(club__id=club_id)
    return JsonResponse(list(coaches.values("id", "name")), safe=False)


def get_court(request):
    data = json.loads(request.body)
    club_id = data["id"]
    courts = Court.objects.filter(club__id=club_id)
    return JsonResponse(list(courts.values("id", "name")), safe=False)


class ReservationShowAllView(View):
    template_name = "reservation/reservation_show_all.html",
    reservations = Reservation.objects.all()

    def get(self, request):
        user = self.request.user
        if self.request.user.is_authenticated:
            reservation = Reservation.objects.filter(user=user.id)
            return render(request, self.template_name, {'reservations': reservation})
        else:
            return render(request, self.template_name, {'clubs': self.reservations})
