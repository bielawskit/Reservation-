from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View


from reservation.forms import ReservationForm
from reservation.models import Reservation

class ReservationAddView(LoginRequiredMixin, View):
    model = Reservation
    template_name = 'reservation/reservation.html'
    form_class = ReservationForm


    def get(self, request):
        form = self.form_class()
        # form.fields['coach'].queryset = models.Coach.objects.filter()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home:home')
        else:
            # form.fields['coach'].queryset = models.Coach.objects.filter()
            return render(request, self.template_name, {'form': form})


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

