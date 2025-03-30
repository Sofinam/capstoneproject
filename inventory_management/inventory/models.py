from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(default=0)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.CharField(max_length=100)
    Date_Added = models.DateTimeField(auto_now=True)
    Last_Updated = models.DateTimeField(auto_now=True)

    # link every item in the inventory to the user who created it
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Inventory', null=True, blank=True)


    def __str__(self):
        return f"{self.name} ({self.quantity} in stock)"
