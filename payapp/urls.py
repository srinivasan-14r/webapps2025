from django.urls import path
from .views import payapp

urlpatterns = [
    path('', payapp, name='payapp'),
]

