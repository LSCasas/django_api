from django.urls import path, include  
from rest_framework import routers
from . import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter() 
router.register(r'owners', viewsets.OwnerViewSet)
router.register(r'species', viewsets.SpeciesViewSet)

urlpatterns = [ 
    path("", include(router.urls)),  
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # <--- CORREGIDO
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
