from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView

from club import forms
from club.models import Club


def club_add(request):
    if request.method == "POST":
        form = forms.ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.ClubForm()

    return render(request, 'club/club_add.html', {'form': form})


def court_add(request):
    if request.method == "POST":
        form = forms.CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.CourtForm()

    return render(request, 'club/court_add.html', {'form': form})




def club_show_all(request):
    clubs = Club.objects.all()

    return render(
        request,
        "club/show_all_clubs.html",
        context={
            'clubs': clubs
        }
    )


class ClubEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Club
    fields = ('name', 'location', 'quantity', 'multisport')
    template_name = 'club/club_edit.html'
    success_url = reverse_lazy('club:club_show_all')
    login_url = reverse_lazy('club:club_show_all')
    permission_required = 'club.change_club'


class ClubDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Club
    success_url = reverse_lazy('club:club_show_all')
    login_url = reverse_lazy('club:club_show_all')
    permission_required = 'club.delete_club'


class ClubDetailsView(DetailView):
    model = Club
    template_name = 'club/club_show_details.html'
    context_object_name = 'club'

    # def get(self, request, club_id):
    #     courts = Court.objects.filter(club_id=club_id)
    #
    #     return render(
    #         request,
    #         'club/club_show_details.html',
    #         context={
    #             'courts': courts
    #         })
