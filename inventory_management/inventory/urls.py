from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import InventoryListView, filtered_inventory_view, register_user, login_user

# Define the url patterns for web based views
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.display_inventory, name='display_inventory'),
    path('create/', views.create_inventory, name='create_inventory'),
    path('update/<int:inventory_id>/', views.update_inventory, name='update_inventory'),
    path('delete/<int:inventory_id>/', views.delete_inventory, name='delete_inventory'),
    path('api/login/', auth_views.LoginView.as_view(template_name='Inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # API end points
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('filtered-inventory/', filtered_inventory_view, name='filtered-inventory'),
    path('register/', register_user, name='api-register'),
    path('api/login/', login_user, name='api-login'),
]
