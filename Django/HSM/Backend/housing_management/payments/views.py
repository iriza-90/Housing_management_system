from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payment
from properties.models import Property
from django.contrib.auth.models import User

@api_view(['POST'])
def make_payment(request):
    try:
        tenant_id = request.data.get('tenant_id')
        property_id = request.data.get('property_id')
        amount = request.data.get('amount')

        tenant = User.objects.get(id=tenant_id)
        property = Property.objects.get(id=property_id)

        payment = Payment.objects.create(
            tenant=tenant,
            property=property,
            amount=amount,
            status='Paid'
        )
        return Response({"message": "Payment successful!", "payment_id": payment.id}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def admin_payments_dashboard(request):
    try:
        payments = Payment.objects.all()
        data = [
            {
                "id": payment.id,
                "tenant": payment.tenant.username,
                "property": payment.property.name,
                "amount": payment.amount,
                "date": payment.date,
                "status": payment.status
            }
            for payment in payments
        ]
        return Response(data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)