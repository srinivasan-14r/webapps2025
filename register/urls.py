from django.urls import path

from payapp import views
from register import views
from . import views

urlpatterns = [
path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),      # Name = 'login'
    path('logout/', views.logout_view, name='logout'),

    path('transfer/', views.transfer_money, name='transfer_money'),
]
