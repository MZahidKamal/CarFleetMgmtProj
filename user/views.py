# All necessary imports for creating views.
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

# Importing all database models from this app.
from .models import ManufacturerAccountModel
from .serializers import (ManufacturerAccountRegistrationSerializer,
                          CarDealerAccountRegistrationSerializer,
                          DeliveryAgentAccountRegistrationSerializer,
                          CustomerAccountRegistrationSerializer)

#-----------------------------------------------------------------------------------------------------------------------

# Create your views here.
"""
@api_view(['GET'])                                                                               # If the method is GET.
def manufacturer_account_list_view(request, format=None):
    try:
        manufacturers = ManufacturerAccountModel.objects.all()
        serializer = ManufacturerAccountModelSerializer(manufacturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])                                               # If the method is GET / PUT / DELETE.
def manufacturer_account_detail_view(request, pk, format=None):
    try:
        manufacturer = ManufacturerAccountModel.objects.get(id=pk)
    except ManufacturerAccountModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ManufacturerAccountModelSerializer(manufacturer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ManufacturerAccountModelSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
#-----------------------------------------------------------------------------------------------------------------------

@api_view(['POST'])                                                                             # If the method is POST.
def common_account_registration_view(request, format=None):
    user_role = request.data.get('user_role')

    # Initially declaring empty serializer to make it accessible outside of if condition.
    serializer = None

    # Depending on the user role, respective serializer will be effective to complete the registration process.
    if user_role == 'MANUFACTURER':
        serializer = ManufacturerAccountRegistrationSerializer(data=request.data)
    elif user_role == 'CAR DEALER':
        serializer = CarDealerAccountRegistrationSerializer(data=request.data)
    elif user_role == 'DELIVERY AGENT':
        serializer = DeliveryAgentAccountRegistrationSerializer(data=request.data)
    elif user_role == 'CUSTOMER':
        serializer = CustomerAccountRegistrationSerializer(data=request.data)

    if serializer.is_valid():

        # Save both the user and manufacturer.
        this_user = serializer.save()
        this_token_key = Token.objects.get(user=this_user).key

        return Response({
            'response': f'{request.data.get('user_role').capitalize()} registered successfully!',
            'token': this_token_key}, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['POST'])                                                                             # If the method is POST.
def common_account_login_view(request, format=None):

    # For login, user_role is not necessary, but I have explicitly included it.
    user_role = request.data.get('user_role')
    username = request.data.get('username')
    password = request.data.get('password')

    this_user = authenticate(username=username, password=password)

    if this_user is not None and this_user.user_role == user_role:
        try:
            this_token = Token.objects.get(user=this_user)
        except Token.DoesNotExist:
            this_token = Token.objects.create(user=this_user)
        return Response({
            'response': 'Login Successful!',
            'token': this_token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# If a token does not exist for the user, a new token will be generated and returned in the response upon successful login.
# If the login attempt fails due to invalid credentials, it returns a proper error response.

# In API testing via Postmann, we'll either provide username and password via Body/form-data or via Body/raw data.

# Without using this common_account_login_view, we may use the "from rest_framework.authtoken.views import obtain_auth_token"
# directly from the urls.py file. But still implemented to see how it actually works.

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['POST'])                                                                             # If the method is POST.
@authentication_classes([TokenAuthentication])                                                  # If the Token is valid.
@permission_classes([IsAuthenticated])                                               # If the user is already logged in.
def common_account_logout_view(request, format=None):
    print(request.data)
    try:
        this_token = Token.objects.get(user=request.user)
        this_token.delete()
        return Response({'response': 'Logout Successful!'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Logout Failed! Please Try Again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# In API testing via Postmann, we'll either provide token key via Headers/Authorization.

#-----------------------------------------------------------------------------------------------------------------------
