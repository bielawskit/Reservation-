import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from club.models import Coach, Court, Club
from reservation.forms import ReservationForm
from reservation.models import Reservation
from users.models import CustomUser


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
            send_email(request)
            data(request)
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


def send_email(request):
    form = ReservationForm(request.POST)
    mail = CustomUser.objects.filter(email=request.user.email).values_list('email', flat=True)
    # mail = list(request.user.email)
    club = Club.objects.get(id=request.POST['club']).name
    court = Court.objects.get(id=request.POST['court']).name
    start = request.POST['start']
    finish = request.POST['finish']
    template_name = "reservation/reservation_show_all.html",
    reservations = Reservation.objects.all()
    email = 'twojtenis555@gmail.com'
    if form.is_valid():
        print(mail)
        message = f"""Potwierdzenie rezerwacji:
                  Obiekt: {club},
                  Kort: {court},
                  Godzina rozpoczęcia: {start} 
                  Godzina zakończenia: {finish}"""
        send_mail(
            'Rezerwacja!',
            message,
            email,
            mail,
            fail_silently=False)
    else:
        return render(request, template_name, {'clubs': reservations})
    return redirect('home:home')

def data(request):
    form = ReservationForm(request.POST)
    start = request.POST['start']
    finish = request.POST['finish']
    if form.is_valid():
        print(start)
        print(finish)