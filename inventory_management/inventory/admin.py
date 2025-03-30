from django.contrib import admin
from .models import Inventory

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Quantity', 'Price', 'Category', 'Date_Added', 'Last_Updated')

