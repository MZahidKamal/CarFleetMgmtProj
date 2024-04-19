# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import DeliveryAgentModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class DeliveryAgentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgentModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
