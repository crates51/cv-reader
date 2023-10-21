import pytest
import unittest


class HelloEndpointTests(unittest.TestCase):

    # pass client from conftest
    @pytest.fixture(autouse = True)
    def prepare_fixture(self, client):
        self.client = client

    def test_01_missing_endpoint(self):
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, None)

    def test_02_api_hello(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        # test same request many slashes
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})
