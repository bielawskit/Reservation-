from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import UpdateView, DeleteView, DetailView
from club import forms, models
from club.models import Club, Coach


# @permission_required('request.user.is_club', login_url=reverse_lazy('users/login_view'))
def club_add(request):
    '''This view generates form to create new club'''
    if request.method == "POST":
        form = forms.ClubForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home:home')
    else:
        form = forms.ClubForm()

    return render(request, 'club/club_add.html', {'form': form})


def court_add(request):
    '''This view generates form to create new court'''
    # user = get_user(request)
    if request.method == "POST":

        form = forms.CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.CourtForm()
        form.fields['club'].queryset = models.Club.objects.filter(user=request.user)
        return render(request=request, template_name='club/court_add.html', context={"form": form})

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


def court_price_list_add(request):
    '''This view generates form to assign a price to court '''
    if request.method == "POST":
        form = forms.PriceListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.PriceListForm()
        form.fields['court'].queryset = models.Club.objects.filter(user=request.user)
    return render(request, 'club/court_price_list_add.html', {'form': form})


def club_show_all(request):
    '''This view generates list with all clubs'''
    clubs = Club.objects.all()

    return render(
        request,
        "club/clubs_show_all.html",
        context={
            'clubs': clubs
        }
    )


class ClubEditView(PermissionRequiredMixin, UpdateView):
    '''This view generates form to change club fields'''
    model = Club
    fields = ('name', 'location', 'quantity', 'multisport')
    template_name = 'club/club_edit.html'
    success_url = reverse_lazy('club:clubShowAll')
    login_url = reverse_lazy('club:clubShowAll')
    permission_required = 'club.change_club'


class ClubDeleteView(PermissionRequiredMixin, DeleteView):
    '''This view generates page to confirm the deletion of the club'''
    model = Club
    success_url = reverse_lazy('club:clubShowAll')
    login_url = reverse_lazy('club:clubDelete')
    permission_required = 'club.delete_club'


class ClubDetailsView(DetailView):
    '''This view generates a page that displays the courts belonging to a particular court '''
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
    '''This view generates a form to create new coach'''
    if request.method == "POST":
        form = forms.CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.CoachForm()
        form.fields['club'].queryset = models.Club.objects.filter(user=request.user)

    return render(request, 'club/court_add.html', {'form': form})


def coach_show_all(request):
    '''This view generates list with all coaches'''
    coach = Coach.objects.all()

    return render(
        request,
        "club/coach_show_all.html",
        context={
            'coach': coach
        }
    )


class CoachEditView(PermissionRequiredMixin, UpdateView):
    '''This view generates form to change coach fields'''
    model = Coach
    fields = ('name', 'surname', 'price', 'club')
    template_name = 'club/coach_edit.html'
    success_url = reverse_lazy('club:coachShowAll')
    login_url = reverse_lazy('club:coachShowAll')
    permission_required = 'club.change_coach'


class CoachDeleteView(PermissionRequiredMixin, DeleteView):
    '''This view generates page to confirm the deletion of the coach'''
    model = Coach
    success_url = reverse_lazy('club:coachShowAll')
    login_url = reverse_lazy('club:coachShowAll')
    permission_required = 'club.delete_coach'

# @permission_required('request.user.is_club', login_url=reverse_lazy('users/login_view'))
