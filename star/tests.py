
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from star.models import Star
class AccountTests(APITestCase):
    def test_create_customer(self):
        url = reverse('star-list')
        data = {
            'id': '1',
            'name': 'Sirio',
            'constellation': 'Canis mayor',
            'absolute_magnitude': 1.42,
            'apparent_magnitude': -1.46,
            'distance': 2.64
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Star.objects.count(), 1)
        self.assertEqual(Star.objects.get().name, 'Sirio')

