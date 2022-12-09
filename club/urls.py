from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('add/', views.club_add, name='clubAdd'),
    path('show/all/clubs', views.club_show_all, name='club_show_all'),
    path('court/add/', views.court_add, name='courtAdd'),
    path('club/edit/<int:pk>/', views.ClubEditView.as_view(), name='ClubEdit'),
    path('club/delete/<int:pk>/', views.ClubDeleteView.as_view(), name='ClubDelete'),
    path('club/details/<int:pk>/', views.ClubDetailsView.as_view(), name='ClubDetails'),


]
