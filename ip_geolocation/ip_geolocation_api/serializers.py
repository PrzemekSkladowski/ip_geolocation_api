from rest_framework import serializers
from .models import GeolocationInfo


class GeolocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeolocationInfo
        fields = ["address", "country", "address_data"]
