from django.shortcuts import render, redirect
from club import forms
from club.models import Club
from django.contrib.auth.decorators import permission_required


@permission_required
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

