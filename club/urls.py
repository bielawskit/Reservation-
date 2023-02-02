from django.urls import path

from . import views


app_name = 'club'

urlpatterns = [
    path('club/add/', views.ClubAddView.as_view(), name='clubAdd'),
    path('clubs/show/all/', views.ClubShowAllView.as_view(), name='clubShowAll'),
    path('club/edit/<int:pk>/', views.ClubEditView.as_view(), name='clubEdit'),
    path('club/delete/<int:pk>/', views.ClubDeleteView.as_view(), name='clubDelete'),
    path('club/details/<int:pk>/', views.ClubDetailsView.as_view(), name='clubDetails'),
    path('court/add/', views.CourtAddView.as_view(), name='courtAdd'),
    path('court/edit/<int:pk>/', views.CourtEditView.as_view(), name='courtEdit'),
    path('court/delete/<int:pk>/', views.CourtDeleteView.as_view(), name='courtDelete'),
    # path('court/price/list/add', views.CourtPriceListAddView.as_view(), name='courtPriceListAdd'),
    # path('court/price/list/add/<int:pk>', views.CourtPriceListAddView.as_view(), name='courtPriceListAdd'),
    path('coach/add/', views.CoachAddView.as_view(), name='coachAdd'),
    path('coach/show/all/', views.CoachShowAllView.as_view(), name='coachShowAll'),
    path('coach/edit/<int:pk>/', views.CoachEditView.as_view(), name='coachEdit'),
    path('coach/delete/<int:pk>/', views.CoachDeleteView.as_view(), name='coachDelete'),

]
