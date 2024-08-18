from django.db import models


class CadastrRecord(models.Model):
    cadastral_number = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    extra_kwargs = {
        'cadastral_number': {'required': True},
        'latitude': {'required': True},
        'longitude': {'required': True},
        }

    def __str__(self):
        return self.cadastral_number
