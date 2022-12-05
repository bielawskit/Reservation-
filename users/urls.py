from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registration_view, name='registration_view'),

]