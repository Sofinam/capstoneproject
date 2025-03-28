from django.shortcuts import render, redirect
from .models import inventory

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


