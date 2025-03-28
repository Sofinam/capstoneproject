from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name
