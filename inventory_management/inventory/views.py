from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import InventorySerializer
from django.db.models import Q


# Create your views here.
# Creating a new inventory
def create_inventory(request):
    if request.method == 'POST':
        name = request.POST['name']
        Inventory.objects.create(name=name)
        return redirect('display_inventory')
    return render(request, 'inventory/create_inventory.html')

# display all the inventory in stock
def display_inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'inventory/display_inventory.html', {'inventory': inventory_items })

# Update inventory
def update_inventory(request, inventory_id):
    inventory_item = get_object_or_404 (Inventory, id=inventory_id)
    if request.method == 'POST':
        inventory_item.name = request.POST['name']
        inventory_item.save()
        return redirect('display_inventory')
    return render(request, 'inventory/update_inventory.html', {'inventory': inventory_item})

#delete item in inventory
def delete_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('display_inventory')
    return render(request, 'inventory/delete_inventory.html', {'inventory': inventory_item})

# implementing CRUD to a logged in user
@login_required
def list_items(request):
    items = Inventory.objects.filter(user=request.user)
    return render(request, 'inventory/item_list.html', {'items: items'})

@login_required
def create_item(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.owner = request.user
        item.save()
        return redirect('item-list')
    return render(request, 'inventory/item_form.html', {'form: form'})

@login_required
def update_item(request, pk):
    item = get_object_or_404(Inventory, pk=pk, owner=request.user)
    form = InventoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item-list')
    return render(request, 'inventory/item_form.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Inventory, pk=pk, owner=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('item-list')
    return render(request, 'inventory/itemm_confirm_delete.html', {'item': item})

class InventoryListView(APIView):
    permission_classes = []

    def get(self, request):
        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)
    
def filtered_inventory_view(request):
    inventory = Inventory.objects.all()

    # filter values from query params
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    low_stock = request.GET.get('low_stock')

    # Apply the filters
    if category:
        inventory = inventory.filter(category__iexact=category)
    if min_price and max_price:
        inventory = inventory.filter(price__gte=min_price, price__lte=max_price)
    if low_stock:
        try:
            threshold = int(low_stock)
            inventory = inventory.filter(quantity__lt=threshold)
        except ValueError:
            pass
    return render(request, 'inventory/filtered_inventory.html', {'inventory': inventory})



