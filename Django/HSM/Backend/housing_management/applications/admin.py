# applications/admin.py
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'status', 'applied_on')
    list_filter = ('status',)
    search_fields = ('tenant__email', 'property__name')
