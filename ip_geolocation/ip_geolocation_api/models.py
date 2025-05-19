from django.db import models


class GeolocationInfo(models.Model):
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address_data = models.JSONField()

    def __str__(self):
        return f'{self.address} from {self.country}'
