from django.urls import path

from . import views

app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.reservation_view, name='reservation_view'),
    path('show/all/reservation/', views.reservation_show_all, name='reservation_show_all'),

]
