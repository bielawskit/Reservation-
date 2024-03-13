import os
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from users import forms


def registration_view(request):
    '''This view generates a form to registrate '''
    if request.method == "POST":
        form = forms.RegistrationFormUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            mail = request.POST.get('email')
            user.save()
            account = get_user_model().objects.get(email=mail)
            group = Group.objects.get(name=os.environ.get('DJ_GROUP_PLAYERS'))
            account.groups.add(group)
            return redirect('users:login_view')
    else:
        form = forms.RegistrationFormUser()

    return render(request, 'users/registration.html', {'form': form})


def registration_view_club(request):
    if request.method == "POST":
        form = forms.RegistrationFormClub(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            mail = request.POST.get('email')
            user.is_club = True
            user.save()
            account = get_user_model().objects.get(email=mail)
            group = Group.objects.get(name=os.environ.get('DJ_GROUP_CLUBS'))
            account.groups.add(group)
            return redirect('users:login_view')
    else:
        form = forms.RegistrationFormClub()

    return render(request, 'users/registration_club.html', {'form': form})


def login_view(request):
    '''This view generates a form to login '''
    if request.method == "POST":
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')
    else:
        form = forms.LoginForm(request)

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """logout"""
    logout(request)
    return redirect('users:login_view')
