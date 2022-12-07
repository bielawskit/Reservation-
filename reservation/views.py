from django.shortcuts import render, redirect

from reservation import forms


def reservation_view(request):
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation:reservation_view')
    else:
        form = forms.ReservationForm()

    return render(request, 'reservation/reservation.html', {'form': form})


