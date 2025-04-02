from django.contrib import admin
from .models import Inventory, InventoryChange

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Quantity', 'Price', 'Category', 'Date_Added', 'Last_Updated')

@admin.register(InventoryChange)
class InventoryChangeAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'change', 'changed_by','timestamp')
    list_filter = ('changed_by', 'timestamp')
    search_fields = ('inventory__name', 'changed_by__username')

