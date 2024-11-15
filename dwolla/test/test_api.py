import os
from unittest.mock import patch

from .. import api
from .base import BaseTestCase


class APITestCase(BaseTestCase):

    def setUp(self):
        super(APITestCase, self).setUp()

    def test_init(self):
        expected = {'a': '1'}
        self.assertEqual(expected,
                         dict(api.API(**{
                             'a': '1'
                         }).__dict__.items()))

    @patch.dict(os.environ, {'API_KEY': '1337'})
    def test_api_key(self):
        self.assertEqual('1337', api.API._api_key())


class OpenWeatherMapAPITestCase(BaseTestCase):

    def setUp(self):
        super(OpenWeatherMapAPITestCase, self).setUp()
        self.mock_requests = patch.object(api, 'requests').start()
        patch.dict(os.environ, {'API_KEY': '1337'}).start()
        self.api = api.OpenWeatherMapAPI()
        self.api.DOMAIN = 'domain'
        self.api.API_PATH = 'path'

    def test_url(self):
        self.assertEqual('https://domain/path', self.api.url)

    def test_get(self):
        self.api._get('url')
        self.mock_requests.get.assert_called_once_with('url')

    def test_get_by_name(self):
        self.api.get_by_name('name')
        self.mock_requests.get.assert_called_once_with(
            'https://domain/path?APPID=1337&q=name')

    def test_get_by_id(self):
        self.api.get_by_id('id')
        self.mock_requests.get.assert_called_once_with(
            'https://domain/path?APPID=1337&id=id')

    def test_get_by_coordinates(self):
        self.api.get_by_coordinates(('0', '0'))
        self.mock_requests.get.assert_called_once_with(
            'https://domain/path?APPID=1337&lat=0&lon=0')

    def test_get_by_zip(self):
        self.api.get_by_zip('12345')
        self.mock_requests.get.assert_called_once_with(
            'https://domain/path?APPID=1337&zip=12345')

    def test_build_url(self):
        expected = 'https://domain/path?APPID=1337&a=1&b=2&c=3'
        self.assertEqual(expected,
                         self.api.build_url({
                             'a': 1,
                             'b': '2',
                             'c': '3'
                         }))
