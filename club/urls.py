from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('add/', views.club_add, name='clubAdd'),
    path('show/all/clubs', views.club_show_all, name='club_show_all'),
    path('court/add/', views.court_add, name='courtAdd'),
]
