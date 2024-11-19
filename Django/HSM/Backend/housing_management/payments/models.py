from django.db import models
from django.conf import settings  # Use settings for user model
from properties.models import Property  

class Payment(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('pending', 'Pending')])

    def __str__(self):
        return f"{self.tenant} - {self.property}"