from rest_framework import serializers
from .models import ccwOrderDetails

class captureOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=ccwOrderDetails
        fields='__all__'