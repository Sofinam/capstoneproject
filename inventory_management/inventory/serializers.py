from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'Name', 'Description', 'Quantity', 'Price', 'Category', 'Date_Added', 'Last_Updated']