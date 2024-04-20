# All necessary imports for creating views.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importing all database models from this app.
from .models import CarDealerModel

# Importing all serializers from this app.
from .serializers import CarDealerModelSerializer

#-----------------------------------------------------------------------------------------------------------------------

# Create your views here.
@api_view(['GET', 'POST'])
def car_dealer_list(request):

    if request.method == 'GET':
        car_dealers = CarDealerModel.objects.all()
        serializer = CarDealerModelSerializer(car_dealers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CarDealerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def car_dealer_details(request, pk):

    try:
        car_dealer = CarDealerModel.objects.get(id=pk)
    except CarDealerModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarDealerModelSerializer(car_dealer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CarDealerModelSerializer(car_dealer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car_dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------
