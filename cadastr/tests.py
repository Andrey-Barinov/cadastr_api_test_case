from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CadastrRecord


class CadastreServiceTests(APITestCase):

    def setUp(self):
        # Создаем тестовые записи
        self.test_record1 = CadastrRecord.objects.create(
            cadastral_number="12:34:5678901:123",
            latitude=55.7558,
            longitude=37.6173,
            result=True
        )
        self.test_record2 = CadastrRecord.objects.create(
            cadastral_number="12:34:5678902:123",
            latitude=55.7558,
            longitude=37.6173,
            result=True
        )

    def test_ping(self):
        """
        Проверка эндпоинта /ping
        """
        url = reverse('ping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Server is running"})

    def test_query(self):
        """
        Проверка эндпоинта /query
        """
        url = reverse('query')
        data = {
            "cadastral_number": "12:34:5678901:456",
            "latitude": 55.7558,
            "longitude": 37.6173
        }
        wrong_data1 = {
            "cadastral_number": "",
            "latitude": 55.7558,
            "longitude": 37.6173,
        }

        wrong_data2 = {
            "cadastral_number": "12:34:5678901:456",
            "latitude": '',
            "longitude": 37.6173,
        }

        wrong_data3 = {
            "cadastral_number": "12:34:5678901:456",
            "latitude": 55.7558,
            "longitude": '',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('pk', response.data)
        self.assertIn('cadastral_number', response.data)
        self.assertIn('latitude', response.data)
        self.assertIn('longitude', response.data)
        self.assertIn('result', response.data)

        response = self.client.post(url, wrong_data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, wrong_data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, wrong_data3, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_result(self):
        """
        Проверка эндпоинта /result
        """
        url = reverse('result')
        data = {
            "cadastral_number": self.test_record1.cadastral_number
        }
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.test_record1.cadastral_number,
            response.data[0]["cadastral_number"]
        )

        response_without_param = self.client.get(url)

        self.assertEqual(response_without_param.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_without_param.data), 2)

    def test_history(self):
        """
        Проверка эндпоинта /history
        """
        url = reverse('history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            self.test_record1.cadastral_number,
            response.data[0]['cadastral_number'])

        self.assertEqual(
            self.test_record2.cadastral_number,
            response.data[1]['cadastral_number']
        )
