from django.core.validators import validate_ipv46_address, validate_domain_name
from django.core.exceptions import ValidationError
from django.db.utils import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GeolocationInfo
from .serializers import GeolocationInfoSerializer
from .services import fetch_geolocation_data_from_external_api


@api_view(['GET'])
def geolocation_all(request):
    try:
        geolocation_info = GeolocationInfo.objects.all()
        serializer = GeolocationInfoSerializer(geolocation_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except OperationalError:
        return Response({'error': 'Database connection lost.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'DELETE'])
def geolocation(request, address):
    try:
        validate_ipv46_address(address)
    except ValidationError:
        try:
            validate_domain_name(address)
        except ValidationError:
            return Response({'message': 'Invalid URL!'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        try:
            geolocation_info = GeolocationInfo.objects.get(address=address)
        except OperationalError:
            return Response({'error': 'Database connection lost.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except GeolocationInfo.DoesNotExist:
            data = fetch_geolocation_data_from_external_api(address)

            if "error" in data:
                return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            new_address = {
                "address": address,
                "country": data.get("country_name", "Unknown"),
                "address_data": data
            }
            serializer = GeolocationInfoSerializer(data=new_address)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = GeolocationInfoSerializer(geolocation_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        try:
            geolocation_info = GeolocationInfo.objects.get(address=address)
            geolocation_info.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GeolocationInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except OperationalError:
            return Response({'error': 'Database connection lost.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
