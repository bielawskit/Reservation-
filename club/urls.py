from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('add/', views.club_add, name='clubAdd'),
    path('show/all/', views.club_add, name='clubAdd'),
]
