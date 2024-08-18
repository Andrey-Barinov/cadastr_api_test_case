from rest_framework import serializers
from .models import CadastrRecord
import random
import time


def get_response_from_an_external_service():
    time.sleep(random.randint(1, 60))
    result = random.choice([True, False])
    return result


class CadastrRecordSerializer(serializers.ModelSerializer):
    result = serializers.BooleanField(read_only=True)

    class Meta:
        model = CadastrRecord
        fields = ['pk', 'cadastral_number', 'latitude', 'longitude', 'result']

    def create(self, validated_data):
        result = get_response_from_an_external_service()
        cadastr_record = CadastrRecord.objects.create(
            cadastral_number=validated_data['cadastral_number'],
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude'],
            result=result
        )
        cadastr_record.save()

        return cadastr_record
