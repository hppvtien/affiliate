
from django.urls import path, include
from SuperAdmin import views



urlpatterns = [
# admin

    path('dashboard/', views.dashboard, name='user-dashboard'),
    path('sign-up/', views.sign_up, name='user-sign-up'),
    path('sign-in/', views.sign_in, name='user-sign-in'),
    path('password-reset/', views.password_reset, name='user-password-reset'),
    path('new-password/', views.new_password, name='user-new-password'),


]


