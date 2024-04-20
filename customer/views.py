# All necessary imports for creating views.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importing all database models from this app.
from .models import CustomerModel

# Importing all serializers from this app.
from .serializers import CustomerModelSerializer

#-----------------------------------------------------------------------------------------------------------------------

# Create your views here.
@api_view(['GET', 'POST'])
def customer_list(request):

    if request.method == 'GET':
        customers = CustomerModel.objects.all()
        serializer = CustomerModelSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CustomerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, pk):

    try:
        customer = CustomerModel.objects.get(id=pk)
    except CustomerModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerModelSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CustomerModelSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------
