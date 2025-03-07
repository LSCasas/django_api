"""API Serializers"""

from rest_framework import serializers
from . import models

class OwnerModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""

    class Meta:
        model = models.Owner  
        fields = ("__str__", "id", "first_name", "last_name", "email", "phone", "mobile")

class SpeciesModelSerializer(serializers.ModelSerializer):  # Corregido el nombre de la clase
    """Species model serializer"""

    class Meta:
        model = models.Species 
        fields = ("id", "name")

class PetModelSerializer(serializers.ModelSerializer):  # Corregido "serializers.ModelSerializers" a "serializers.ModelSerializer"
    """Pet model serializer"""
    
    class Meta:
        model = models.Pet  
        fields = ("id", "name", "owner", "age", "species", "created_at")

class RecordModelSerializer(serializers.ModelSerializer):  # Corregido "serializers.ModelSerialiezer" a "serializers.ModelSerializer"
    """Record model serializer"""
    
    class Meta:
        model = models.Record
        fields = ("id", "category", "produce", "pet", "date")