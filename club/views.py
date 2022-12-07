from django.shortcuts import render, redirect

from club import forms


def club_add(request):
    if request.method == "POST":
        form = forms.ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = forms.ClubForm()

    return render(request, 'club/club_add.html', {'form': form})
