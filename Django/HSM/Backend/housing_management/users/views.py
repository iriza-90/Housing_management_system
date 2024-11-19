import json
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser  

@api_view(['POST'])
def signup(request):
    """
    Handles user signup. Creates a new user with the data provided.
    """
    data = request.data
    first_name = data.get('firstName')  # Frontend uses firstName
    last_name = data.get('lastName')    # Frontend uses lastName
    email = data.get('email')
    phone_number = data.get('phoneNumber')  # Frontend uses phoneNumber
    password = data.get('password')
    role = data.get('registerAs')  # Frontend uses registerAs

    if not all([ first_name, last_name, email, phone_number,password, role]):
        return Response({"error": "All fields are required!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role=role
        )
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """
    Handles user login. Authenticates the user and returns a JWT token if successful.
    """
    if request.method == 'POST':
        data = request.data
        
        email = data.get('email')
        password = data.get('password')

        # Authenticating user using email and password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({
                "message": "Login successful",
                "access_token": str(access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
