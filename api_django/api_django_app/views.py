from rest_framework import generics, status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ItemListCreateView(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def post(self, request, *args, **kwargs):
        if 'price' not in request.data:
            return Response({'error': 'O atributo "price" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            price = float(request.data['price'])
            if price <= 0:
                return Response({'error': 'O atributo "price" deve ser maior que zero.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'O atributo "price" deve ser um número válido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        
        return super().list(request, *args, **kwargs)
