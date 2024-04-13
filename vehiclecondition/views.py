# All necessary imports for creating views.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importing all database models from this app.
from .models import (VehicleConditionModel,
                     CarReceivingVCModel,
                     CarGivingVCModel)

# Importing all serializers from this app.
from .serializers import (ProofImagesModelSerializer,
                          VehicleConditionModelSerializer,
                          CarReceivingVCModelSerializer,
                          CarGivingVCModelSerializer)

#-----------------------------------------------------------------------------------------------------------------------

# Create your views here.
@api_view(['GET', 'POST'])
def vehicle_condition_list(request, format=None):

    if request.method == 'GET':
        vc_reports = VehicleConditionModel.objects.all()
        serializer = VehicleConditionModelSerializer(vc_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = VehicleConditionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_condition_detail(request, pk, format=None):
    try:
        vc_report = VehicleConditionModel.objects.get(id=pk)
    except VehicleConditionModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleConditionModelSerializer(vc_report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = VehicleConditionModelSerializer(vc_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vc_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def car_receiving_vc_list(request, format=None):

    if request.method == 'GET':
        car_receiving_vc_reports = CarReceivingVCModel.objects.all()
        serializer = CarReceivingVCModelSerializer(car_receiving_vc_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CarReceivingVCModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def car_receiving_vc_detail(request, pk, format=None):
    try:
        car_receiving_vc_report = CarReceivingVCModel.objects.get(id=pk)
    except CarReceivingVCModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarReceivingVCModelSerializer(car_receiving_vc_report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CarReceivingVCModelSerializer(car_receiving_vc_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car_receiving_vc_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def car_giving_vc_list(request, format=None):

    if request.method == 'GET':
        car_giving_vc_reports = CarGivingVCModel.objects.all()
        serializer = CarGivingVCModelSerializer(car_giving_vc_reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CarGivingVCModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def car_giving_vc_detail(request, pk, format=None):
    try:
        car_giving_vc_report = CarGivingVCModel.objects.get(id=pk)
    except CarGivingVCModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarGivingVCModelSerializer(car_giving_vc_report)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CarGivingVCModelSerializer(car_giving_vc_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car_giving_vc_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------
