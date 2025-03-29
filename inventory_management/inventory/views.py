from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import inventory
from .forms import inventoryform


# Create your views here.
# Creating a new inventory
def create_inventory(request):
    if request.method == 'POST':
        name = request.POST['name']
        inventory.objects.create(name=name)
        return redirect('list_inventory')
    return render(request, 'inventory/create_inventory.html')

# display all the inventory in stock
def display_inventory(request):
    inventory = inventory.objects.all()
    return render(request, 'inventory/display_inventory.html', {'inventory': inventory })

# Update inventory
def update_inventory(request, inventory_id):
    invetory = inventory.objects.get(id=inventory_id)
    if request.method == 'POST':
        inventory.name = request.POST['name']
        inventory.completed = 'completed' in request.POST
        inventory.save()
        return redirect('display_inventory')
    return render(request, 'inventory/update_inventory.html', {'inventory': inventory})

#delete inventory
def delete_inventory(request, inventory_id):
    inventory = inventory.objects.get(id=inventory_id)
    inventory.delete()
    return redirect('display_inventory')

# implementing CRUD to a logged in user
@login_required
def list_items(request):
    items = inventory.objects.filter(user=request.user)
    return render(request, 'inventory/item_list.html', {'items: items'})

@login_required
def create_item(request):
    form = inventoryform(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('item-list')
    return render(request, 'inventory/item_form.html', {'form: form'})

@login_required
def update_item(request, pk):
    item = get_object_or_404(inventory, pk=pk, user=request.user)
    form = inventoryform(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item-list')
    return render(request, 'inventory/item_form.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(inventory, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('item-list')
    return render(request, 'inventory/itemm_confirm_delete.html', {'item': item})



