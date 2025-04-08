from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),      # Name = 'login'
    path('logout/', views.logout_view, name='logout'),    # Custom logout view
]
