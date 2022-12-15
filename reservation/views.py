from django.shortcuts import render, redirect
from reservation import forms
from reservation.models import Reservation


def reservation_view(request):
    '''This view generates form to book court'''
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation:reservation_view')
    else:
        form = forms.ReservationForm()

    return render(request, 'reservation/reservation.html', {'form': form})


def reservation_show_all(request):
    '''This view generates a list with bookings of the user on courts'''
    reservations = Reservation.objects.all()

    return render(
        request,
        "reservation/show_all_reservation.html",
        context={
            'reservations': reservations,
        }
    )
