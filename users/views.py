import os

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from users import forms
from users.models import CustomUser


def registration_view(request):
    '''This view generates a form to registrate '''
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            mail = request.POST.get('email')
            account = get_user_model().objects.get(email=mail)
            if user.is_club:
                group = Group.objects.get(name=os.environ.get('DJ_GROUP_CLUBS'))
            else:
                group = Group.objects.get(name=os.environ.get('DJ_GROUP_PLAYERS'))
            account.groups.add(group)
            user.save()
            return redirect('users:login_view')
    else:
        form = forms.RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


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


def send_mail(request):
    mail = CustomUser.objects.get(email=request.user).email
