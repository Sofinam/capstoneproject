from django.urls import path
from .import views

# Define the url patterns
urlpatterns = [
    path('', views.display_inventory, name='display_inventory'),
    path('create/', views.create_inventory, name='create_inventory'),
    path('update/<int:inventory_id>/', views.update_inventory, name='update_inventory'),
    path('delete/<int:inventory_id/', views.delete_inventory, name='delete_inventory'),
]
