"""REST API viewsets"""

from rest_framework import viewsets
from . import models, serializers  

class OwnerViewSet(viewsets.ModelViewSet):
    """Owner objetct"""

    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerModelSerializer 

class SpeciesViewSet(viewsets.ModelViewSet):  
    """Species viewset"""

    queryset = models.Species.objects.all()
    serializer_class = serializers.SpeciesModelSerializer  

class PetViewSet(viewsets.ModelViewSet):
    """Record viewset"""

    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordModelSerializer

class RecordViewSet(viewsets.ModelViewSet):
    """Record viewset"""

    queryset = models.Record.objects.all()
    serializers_class = serializers.RecordModelSerializer