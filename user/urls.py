
from django.urls import path, include
from user import views




urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.login, name='user-login'),
    path('logout/', views.logout, name='user-logout'),
    path('accounts/', include('allauth.urls'), name='user-login-auth'),
    path('profile/', views.profile_user, name='user-profile'),
    path('chanels/', views.chanel, name='user-chanel'),
    path('update/', views.update_user, name='update-user'),
    path('created_index/', views.create_index_user, name='create-index-user'),
    path('created/', views.create_share_user, name='create-share-user'),
    path('edit_share/<int:id>', views.edit_share_user, name='edit-share-user'),
    path('update_share/<int:id>', views.update_share_user, name='update-share-user'),
    path('delete_share/<int:id>', views.delete_share_user, name='delete-share-user'),
    path('short_link', views.short_link, name='short-link'),
    path('count_view', views.count_view, name='count-view'),
    path('real_link', views.real_link, name='real-link'),
]
