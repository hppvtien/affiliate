
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', views.index, name='home'),
    path('user/', include('user.urls'), name='user'),
    path('admin/', include('SuperAdmin.urls'), name='admin'), 
)
