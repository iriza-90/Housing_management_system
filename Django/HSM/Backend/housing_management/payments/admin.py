from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'amount', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('tenant__username', 'property__name')