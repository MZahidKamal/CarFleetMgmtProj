# All necessary imports for creating views.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importing all database models from this app.
from .models import DeliveryAgentModel

# Importing all serializers from this app.
from .serializers import DeliveryAgentModelSerializer

#-----------------------------------------------------------------------------------------------------------------------

# Create your views here.
@api_view(['GET', 'POST'])
def delivery_agent_list(request):

    if request.method == 'GET':
        delivery_agents = DeliveryAgentModel.objects.all()
        serializer = DeliveryAgentModelSerializer(delivery_agents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DeliveryAgentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def delivery_agents_details(request, pk):

    try:
        delivery_agent = DeliveryAgentModel.objects.get(id=pk)
    except DeliveryAgentModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeliveryAgentModelSerializer(delivery_agent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DeliveryAgentModelSerializer(delivery_agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        delivery_agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------
