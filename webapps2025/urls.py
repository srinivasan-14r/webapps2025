from django.contrib import admin
from django.urls import path, include
from register.views import register_view, home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapps2025/', include('register.urls')),  # Clean & modular
    path('webapps2025/register/', register_view, name='register'),
    path('home/', home_view, name='home'),

]
