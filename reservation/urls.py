from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.ReservationAddView.as_view(), name='reservation_view'),
    path('get_coach/', views.get_coach, name='get_coach'),
    path('get_court/', views.get_court, name='get_court'),
    path('show/all/reservation/', views.ReservationShowAllView.as_view(), name='reservation_show_all'),

]
