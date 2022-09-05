from django.test import TestCase

from rest_framework import status

from unittest import mock
# Create your tests here.

class TestApiCall(TestCase):
    def setUp(self):
        self.baseurl='http://localhost:8000/artist?name='

    def test_artist_info(self):
        url = self.baseurl + 'coldplay'
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK


    def test_artist_info_bad_request(self):
        url = self.baseurl + 'coldplay1234'
        response = self.client.get(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
