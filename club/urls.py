from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('club/add/', views.club_add, name='clubAdd'),
    path('clubs/show/all/', views.club_show_all, name='clubShowAll'),
    path('club/edit/<int:pk>/', views.ClubEditView.as_view(), name='clubEdit'),
    path('club/delete/<int:pk>/', views.ClubDeleteView.as_view(), name='clubDelete'),
    path('club/details/<int:pk>/', views.ClubDetailsView.as_view(), name='clubDetails'),
    path('court/add/', views.court_add, name='courtAdd'),
    path('coach/add/', views.coach_add, name='coachAdd'),
    path('coach/show/all/', views.coach_show_all, name='coachShowAll'),




]
