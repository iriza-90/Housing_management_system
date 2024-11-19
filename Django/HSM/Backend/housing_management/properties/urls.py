from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.get_properties, name='get_properties'),
    path('properties/create/', views.create_property, name='create_property'),
    path('properties/<int:pk>/update/', views.update_property, name='update_property'),
    path('properties/<int:pk>/delete/', views.delete_property, name='delete_property'),
]

