from django.urls import path
from . import views

urlpatterns = [
    path('make/', views.make_payment, name='make_payment'),
    path('admin_dashboard/', views.admin_payments_dashboard, name='admin_payments_dashboard'),
]