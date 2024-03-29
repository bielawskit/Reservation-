import json

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView

from club import models
from club.forms import ClubForm, CourtForm, CoachForm, CoachFormEdit
from club.models import Club, Coach, Court


class ClubAddView(LoginRequiredMixin, View):
    template_name = "club/club_add.html"
    form_class = ClubForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("home:home")
        else:
            return render(request, self.template_name, {"form": form})


class ClubSortedView(View):
    template_name = "club/clubs_sorted.html"
    clubs = Club.objects.all()

    def get(self, request):
        user = self.request.user
        group = user.groups.filter(name="clubs").exists()
        if user.is_authenticated and group:
            club = Club.objects.filter(user=user.id).order_by("name")
            return render(request, self.template_name, {"clubs": club})
        else:
            return render(request, self.template_name, {"clubs": self.clubs})


class ClubShowAllView(View):
    template_name = "club/clubs_show_all.html"

    def get(self, request):
        return render(request, self.template_name, {"clubs": Club.objects.all()})


class ClubEditView(PermissionRequiredMixin, UpdateView):
    model = Club
    fields = ("name", "location", "quantity", "multisport")
    template_name = "club/club_edit.html"
    success_url = reverse_lazy("club:clubShowAll")
    login_url = reverse_lazy("club:clubShowAll")
    permission_required = "club.change_club"


class ClubDeleteView(PermissionRequiredMixin, DeleteView):
    """This view generates page to confirm the deletion of the club"""

    model = Club
    success_url = reverse_lazy("club:clubShowAll")
    login_url = reverse_lazy("club:clubDelete")
    permission_required = "club.delete_club"


class ClubDetailsView(DetailView):
    """This view generates a page that displays the courts belonging to a particular court"""

    model = Club
    template_name = "club/club_show_details.html"
    context_object_name = "club"


class CourtAddView(LoginRequiredMixin, View):
    template_name = "club/court_add.html"
    form_class = CourtForm

    def get(self, request):
        form = self.form_class()
        form.fields["club"].queryset = models.Club.objects.filter(user=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("home:home")
        else:
            form = self.form_class()
            form.fields["club"].queryset = models.Club.objects.filter(user=request.user)
            return render(request, self.template_name, {"form": form})


def get_court(request):
    data = json.loads(request.body)
    club_id = data["id"]
    courts = Court.objects.filter(club__id=club_id)
    return JsonResponse(list(courts.values("id", "name")), safe=False)


class CourtEditView(PermissionRequiredMixin, UpdateView):
    model = Court
    fields = ("club", "name", "type", "preference", "cost")
    template_name = "club/court_edit.html"
    success_url = reverse_lazy("club:clubShowAll")
    login_url = reverse_lazy("club:clubShowAll")
    permission_required = "club.change_court"


class CourtDeleteView(PermissionRequiredMixin, DeleteView):
    model = Court
    success_url = reverse_lazy("club:clubShowAll")
    login_url = reverse_lazy("club:courtDelete")
    permission_required = "club.delete_court"


class CoachAddView(View):
    template_name = "club/coach_add.html"
    form_class = CoachForm

    def get(self, request):
        form = self.form_class()
        form.fields["club"].queryset = models.Club.objects.filter(user=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("home:home")
        else:
            form.fields["club"].queryset = models.Club.objects.filter(user=request.user)
            return render(request, self.template_name, {"form": form})


class CoachShowAllView(View):
    template_name = "club/coach_show_all.html"

    def get(self, request):
        user = self.request.user
        group = user.groups.filter(name="clubs").exists()
        if user.is_authenticated and group:
            coach = Coach.objects.filter(user=user.id)
        else:
            coach = Coach.objects.all()
        return render(request, self.template_name, {"coach": coach})


class CoachEditView(PermissionRequiredMixin, UpdateView):
    model = Coach
    form_class = CoachFormEdit
    template_name = "club/coach_edit.html"
    success_url = reverse_lazy("club:coachShowAll")
    login_url = reverse_lazy("club:coachShowAll")
    permission_required = "club.change_coach"

    def get_form_kwargs(self):
        kwargs = super(CoachEditView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CoachDeleteView(PermissionRequiredMixin, DeleteView):
    """This view generates page to confirm the deletion of the coach"""

    model = Coach
    success_url = reverse_lazy("club:coachShowAll")
    login_url = reverse_lazy("club:coachShowAll")
    permission_required = "club.delete_coach"
