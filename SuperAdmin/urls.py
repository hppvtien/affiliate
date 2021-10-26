
from django.urls import path, include
from SuperAdmin import views



urlpatterns = [
# admin

    path('dashboard/', views.dashboard, name='user-dashboard'),
    path('sign-up/', views.sign_up, name='user-sign-up'),
    path('sign-in/', views.sign_in, name='user-sign-in'),
    path('password-reset/', views.password_reset, name='user-password-reset'),
    path('new-password/', views.new_password, name='user-new-password'),


    path('user-admin/', views.user_admin, name='user-admin'),
    path('user-admin-create/', views.user_admin_create, name='user-admin-create'),
    path('user-admin-store/', views.user_admin_store, name='user-admin-store'),
    path('user-admin-edit/<int:id>', views.user_admin_edit, name='user-admin-edit'),
    path('user-admin-update/<str:id>', views.user_admin_update, name='user-admin-update'),
    path('user-admin-delete/<str:id>', views.user_admin_delete, name='user-admin-delete'),


]


