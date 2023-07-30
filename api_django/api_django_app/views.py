from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
