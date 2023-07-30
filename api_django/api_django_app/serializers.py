from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    
    class Meta:
        model = Item
        fields = '__all__'
        