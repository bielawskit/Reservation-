from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registration_view, name='registration_view'),
    path('register/club', views.registration_view_club, name='registration_view_club'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

]