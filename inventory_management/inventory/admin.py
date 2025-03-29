from django.contrib import admin
from .models import inventory

# Register your models here.
@admin.register(inventory)
class inventoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Quantity', 'Price', 'Category', 'Date_Added', 'Last_Updated')

