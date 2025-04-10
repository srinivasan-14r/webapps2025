from django.contrib import admin
from django.urls import path, include
from register.views import register_view, home_view
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='webapps2025/')),
    path('webapps2025/', include('register.urls')),  # Clean & modular
    path('webapps2025/register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    path('payapp/', include('payapp.urls')),
]
