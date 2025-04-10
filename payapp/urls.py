from django.urls import path
from . import views

urlpatterns = [
    path('', views.payapp, name='payapp'),
    path('make-payment/', views.make_payment_view, name='make_payment'),
    path('request_money/', views.request_money_view, name='request_money'),
    path('transactions/', views.transaction_history_view, name='transaction_history'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),



]

