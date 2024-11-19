# applications/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from properties.models import Property
from applications.models import Application


@api_view(['GET'])
def list_properties(request):
    """
    List all available properties.
    """
    properties = Property.objects.filter(available=True)
    data = [
        {
            "id": p.id,
            "name": p.name,
            "address": p.address,
            "rent_price": str(p.rent_price),
            "size": p.size,
            "available": p.available,
        }
        for p in properties
    ]
    return Response(data)
@api_view(['POST'])
def apply_for_property(request):
    """
    Tenant applies for a property.
    """
    tenant = request.user
    property_id = request.data.get("property_id")
    message = request.data.get("message", "")

    if not property_id:
        return Response({"error": "Property ID is required"}, status=400)

    try:
        property_obj = Property.objects.get(id=property_id, available=True)
        application = Application.objects.create(tenant=tenant, property=property_obj, message=message)
        return Response({"message": "Application submitted successfully", "application_id": application.id})
    except Property.DoesNotExist:
        return Response({"error": "Property not found or not available"}, status=404)

@api_view(['GET'])
def list_applications(request):
    """
    List all applications for all properties.
    """
    applications = Application.objects.all()
    data = [
        {
            "id": app.id,
            "tenant": app.tenant.email,
            "property": app.property.name,
            "message": app.message,
            "status": app.status,
            "applied_on": app.applied_on,
        }
        for app in applications
    ]
    return Response(data)

@api_view(['POST'])
def update_application_status(request):
    """
    Approve or reject an application.
    """
    application_id = request.data.get("application_id")
    status = request.data.get("status")  # 'approved' or 'rejected'

    if status not in ['approved', 'rejected']:
        return Response({"error": "Invalid status"}, status=400)

    try:
        application = Application.objects.get(id=application_id)
        if application.status != 'pending':
            return Response({"error": "Application already processed"}, status=400)
        application.status = status
        application.save()
        if status == 'approved':
            application.property.available = False
            application.property.save()
        return Response({"message": f"Application {status} successfully"})
    except Application.DoesNotExist:
        return Response({"error": "Application not found"}, status=404)
