# applications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list-properties/', views.list_properties, name='list_properties'),
    path('apply/', views.apply_for_property, name='apply_for_property'),
    path('list-applications/', views.list_applications, name='list_applications'),
    path('update-status/', views.update_application_status, name='update_application_status'),
]
