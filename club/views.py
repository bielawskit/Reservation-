from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import UpdateView, DeleteView, DetailView
from club import forms, models
from club.models import Club, Coach


def club_add(request):
    if request.method == "POST":
        form = forms.ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.ClubForm()

    return render(request, 'club/club_add.html', {'form': form})


# class CourtAddView(View):
#
#     def get(self, request):
#         return render(request, 'club/court_add.html', {'form': form})
#
#     def post(self, request):
#         form = forms.CourtForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home:home')
#
#         return render(request, 'club/court_add.html', {'form': form})
def court_add(request):
    user = get_user(request)
    if request.method == "POST":

        form = forms.CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.CourtForm()
        form.fields['club'].queryset = models.Court.objects.filter(user=user) # request.user
        return render(request=request, template_name='club/court_add.html', context={"form": form})


def court_price_list_add(request):
    if request.method == "POST":
        form = forms.PriceListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.PriceListForm()

    return render(request, 'club/court_price_list_add.html', {'form': form})


def club_show_all(request):
    clubs = Club.objects.all()

    return render(
        request,
        "club/clubs_show_all.html",
        context={
            'clubs': clubs
        }
    )


class ClubEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Club
    fields = ('name', 'location', 'quantity', 'multisport')
    template_name = 'club/club_edit.html'
    success_url = reverse_lazy('club:clubShowAll')
    login_url = reverse_lazy('club:clubShowAll')
    permission_required = 'club.change_club'


class ClubDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Club
    success_url = reverse_lazy('club:clubShowAll')
    login_url = reverse_lazy('club:clubDelete')
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


def coach_add(request):
    if request.method == "POST":
        form = forms.CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.CoachForm()

    return render(request, 'club/court_add.html', {'form': form})


def coach_show_all(request):
    coach = Coach.objects.all()

    return render(
        request,
        "club/coach_show_all.html",
        context={
            'coach': coach
        }
    )


class CoachEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Coach
    fields = ('name', 'surname', 'price', 'club')
    template_name = 'club/coach_edit.html'
    success_url = reverse_lazy('club:coachShowAll')
    login_url = reverse_lazy('club:coachShowAll')
    permission_required = 'coach.change_coach'


class CoachDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Coach
    success_url = reverse_lazy('club:coachShowAll')
    login_url = reverse_lazy('club:coachShowAll')
    permission_required = 'coach.delete_coach'


