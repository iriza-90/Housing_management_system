from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
