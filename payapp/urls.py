from django.urls import path
from . import views

urlpatterns = [
    path('', views.payapp, name='payapp'),
    path('make-payment/', views.make_payment_view, name='make_payment'),
    path('request_money/', views.request_money_view, name='request_money'),


]

