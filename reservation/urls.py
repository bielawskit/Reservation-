from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.ReservationAddView.as_view(), name='reservation_view'),
    # path('reservations/', views.Reservation, name='reservation_view'),
    path('get_coach/', views.get_coach, name='get_coach'),
    path('show/all/reservation/', views.ReservationShowAllView.as_view(), name='reservation_show_all'),

]
