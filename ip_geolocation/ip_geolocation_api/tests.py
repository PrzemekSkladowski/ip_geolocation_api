from rest_framework.test import APITestCase
from rest_framework import status
from .models import GeolocationInfo


class GeolocationInfoAPITestCase(APITestCase):
    def setUp(self):
        address_data = {"region_code": "WA", "region_name": "Warsaw", "country_code": "PL", "country_name": "Poland"}
        GeolocationInfo.objects.create(address="194.0.0.1", country="Poland", address_data=address_data)
        address_data_2 = {"region_code": "RK", "region_name": "Reykjavik", "country_code": "IS", "country_name": "Iceland"}
        GeolocationInfo.objects.create(address="194.0.0.2", country="Iceland", address_data=address_data_2)
        address_data_3 = {"region_code": "FR", "region_name": "Firenze", "country_code": "IT", "country_name": "Italy"}
        GeolocationInfo.objects.create(address="194.0.0.3", country="Italy", address_data=address_data_3)

    def test_get_all_geolocation_infos(self):
        """Test retrieving a list of items"""
        response = self.client.get("/geolocation/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(response.json()[0]["address"], ["194.0.0.1", "194.0.0.2", "194.0.0.3"])
        self.assertIn(response.json()[0]["country"], ["Poland", "Iceland", "Italy"])
        self.assertIn(response.json()[0]["address_data"]["region_name"], ["Warsaw", "Reykjavik", "Firenze"])

    def test_get_geolocation_by_address(self):
        """Test retrieving an item by address"""
        response = self.client.get("/geolocation/194.0.0.1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("194.0.0.1", response.json()["address"])
        self.assertIn("Poland", response.json()["country"])
        self.assertIn("Warsaw", response.json()["address_data"]["region_name"])

        response = self.client.get("/geolocation/194.0.0.2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("194.0.0.2", response.json()["address"])
        self.assertIn("Iceland", response.json()["country"])
        self.assertIn("Reykjavik", response.json()["address_data"]["region_name"])

    def test_delete_geolocation_by_address(self):
        """Test deleting an item by address"""
        response = self.client.delete("/geolocation/194.0.0.3")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get("/geolocation/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
