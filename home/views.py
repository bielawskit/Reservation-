from django.shortcuts import render

from django.shortcuts import render
from club.models import Club, Court
from reservation.models import Reservation
from users.models import CustomUser


def home(request):
    number_of_clubs = Club.objects.count()
    print(number_of_clubs)
    number_of_courts = Court.objects.count()
    number_of_reservations = Reservation.objects.count()
    number_of_users = CustomUser.objects.count()

    context = {
        'number_of_clubs': number_of_clubs,
        'number_of_courts': number_of_courts,
        'number_of_reservations': number_of_reservations,
        'number_of_users': number_of_users,
    }

    return render(request, 'home/home.html', context)
