from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Property

# Get all properties
@csrf_exempt
def get_properties(request):
    properties = Property.objects.all().values()  # Convert QuerySet to a list of dictionaries
    return JsonResponse(list(properties), safe=False)

# Create a new property
@csrf_exempt  
def create_property(request):
    if request.method == 'POST':
        data = json.loads(request.body)  
        property = Property.objects.create(
            name=data.get('name'),
            address=data.get('address'),
            rent_price=data.get('rent_price'),
            size=data.get('size'),
            available=data.get('available', True)
        )
        return JsonResponse({"id": property.id, "message": "Property created successfully!"}, status=201)

# Update a property
@csrf_exempt
def update_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)
    if request.method == 'PUT':
        data = json.loads(request.body)
        property.name = data.get('name', property.name)
        property.address = data.get('address', property.address)
        property.rent_price = data.get('rent_price', property.rent_price)
        property.size = data.get('size', property.size)
        property.available = data.get('available', property.available)
        property.save()
        return JsonResponse({"message": "Property updated successfully!"})

# Delete a property
@csrf_exempt
def delete_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)
    if request.method == 'DELETE':
        property.delete()
        return JsonResponse({"message": "Property deleted successfully!"}, status=204)
