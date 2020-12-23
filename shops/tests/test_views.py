from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ShopsViewSetTest(APITestCase):
    fixtures = ['address/fixtures/initial_data.json', 'shops/fixtures/initial_data.json']

    def test_shop_list(self):
        url = reverse('shops-list')
        response = self.client.get(url, {'ordering': 'name'})
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 2)
        self.assertEqual(response_json,
                         [{'id': 2, 'name': 'Книги', 'city': 'Ульяновск', 'street': 'Ленина', 'house': '1',
                           'time_open': '08:27:27', 'time_close': '18:00:00'},
                          {'id': 1, 'name': 'Магнит', 'city': 'Москва', 'street': 'Ленина', 'house': '1',
                           'time_open': '06:00:00', 'time_close': '18:00:00'}])
