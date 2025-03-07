"""REST API viewsets"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    @action(detail=false)
    def auth(setf, request):
        """Logica de autentificacion"""
        return Response({"token": token})
    
    @action(detail=False)
    def create(self, request):
        """Se genera un nuevo usuario"""
        return 

class OwnerViewSet(viewsets.MdeolViewSet):
    """Owner viewset"""

    queryset = models.Owner.objects.all()
    seializer_class = seializers.OwnerModelSerializer

class SpeciesViewSet(viewsets.Model):
    """Species viewset"""

    queryset = models.Species.objects.all()
    serializer_class = serializer.SpeciesModelSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Record viewset"""

    query = models.Record.objects.all()
    serializer_class = serializers.RecordModelSerializer