from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CitiesViewSetTest(APITestCase):
    fixtures = ['address/fixtures/initial_data.json', ]

    def test_city_list(self):
        url = reverse('city-list')
        response = self.client.get(url, {'ordering': 'name'})
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 4)
        self.assertEqual(response_json,
                         [{'name': 'Казань'}, {'name': 'Москва'}, {'name': 'Самара'}, {'name': 'Ульяновск'}])

    def test_street_list(self):
        url = reverse('city-list_streets', kwargs={'pk': 1})
        response = self.client.get(url, {'ordering': 'name'})
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 3)
        self.assertEqual(response_json,
                         [{'name': 'Ленина'}, {'name': 'Станиславского'}, {'name': 'Трофимова'}])
