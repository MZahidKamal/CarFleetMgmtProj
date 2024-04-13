# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import CarExpensesModel, OverheadExpensesModel, WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class CarExpensesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarExpensesModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class OverheadExpensesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverheadExpensesModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class WorkOrdersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrdersModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
