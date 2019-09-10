"""Module for interacting with the OpenWeatherMap API."""
import os

import requests


class API(object):
    """Base API class."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize object."""
        self.__dict__.update(kwargs)

    @classmethod
    def _api_key(cls) -> dict:
        """
        Get the API key.

        :returns: API key
        :rtype: str
        """
        return os.environ['API_KEY']


class OpenWeatherMapAPI(API):
    """Class for interacting with the OpenWeatherMap API."""

    DOMAIN = 'api.openweathermap.org'
    API_PATH = 'data/2.5/weather'

    def __init__(self, *args, **kwargs) -> None:
        """Initialize object."""
        super(API, self).__init__()

    @property
    def url(cls) -> str:
        """URL of the OpenWeatherMap API."""
        return '{protocol}://{domain}/{api_path}'.format(
            protocol='https', domain=cls.DOMAIN, api_path=cls.API_PATH)

    def _get(self, url: str) -> requests.Response:
        r = requests.get(url)
        r.raise_for_status()
        return r

    def get_by_name(self, name: str) -> dict:
        """
        Retrieve the current weather data for a city using the city name.

        :param name: name of the city
        :type name: str
        """
        url = self.build_url({'q': name})
        r = self._get(url)
        return r.json()

    def get_by_id(self, _id: str) -> dict:
        """
        Retrieve the current weather data for a city using the city ID.

        :param _id: ID of the city
        :type _id: str
        """
        url = self.build_url({'id': _id})
        r = self._get(url)
        return r.json()

    def get_by_coordinates(self, coordinates: tuple) -> dict:
        """
        Retrieve the current weather data for a city using coordinates.

        :param coordinates: coordinates of the city
        :type coordinates: tuple
        """
        url = self.build_url({'lat': coordinates[0], 'lon': coordinates[1]})
        r = self._get(url)
        return r.json()

    def get_by_zip(self, _zip: str) -> dict:
        """
        Retrieve the current weather data for a city using the ZIP code.

        :param _zip: zip code of the city
        :type _zip: str
        """
        url = self.build_url({'zip': _zip})
        r = self._get(url)
        return r.json()

    def build_url(self, parameters=None) -> str:
        """
        Build a URL.

        :param parameters: optional GET parameters
        :type parameters: dict
        :return: URL
        :rtype: str
        """
        parameters.update({'APPID': self._api_key()})
        url = '{}{}'.format(self.url, '?')
        for key, value in sorted(parameters.items()):
            parameter = '{key}={value}&'.format(key=key, value=value)
            url = '{}{}'.format(url, parameter)
        return url[:-1]
