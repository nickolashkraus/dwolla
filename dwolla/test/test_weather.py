from unittest.mock import Mock, patch

from click.testing import CliRunner

from .. import weather
from ..cli import cli
from .base import BaseTestCase


class WeatherTestCase(BaseTestCase):
    def setUp(self):
        super(WeatherTestCase, self).setUp()
        self.runner = CliRunner()
        self.api = Mock()
        self.mock_api = patch.object(weather, 'OpenWeatherMapAPI').start()
        self.mock_api.return_value = self.api

    def test_weather(self):
        # test name option
        result = self.runner.invoke(cli, ['weather', '--name', 'Chicago'])
        self.assertIs(None, result.exception)
        self.assertEqual(0, result.exit_code)
        self.api.get_by_name.assert_called_once_with('Chicago')

        # test id option
        result = self.runner.invoke(cli, ['weather', '--id', '4887442'])
        self.assertIs(None, result.exception)
        self.assertEqual(0, result.exit_code)
        self.api.get_by_id.assert_called_once_with('4887442')

        # test coordinates option
        result = self.runner.invoke(
            cli, ['weather', '--coordinates', '41.85', '-87.65'])
        self.assertIs(None, result.exception)
        self.assertEqual(0, result.exit_code)
        self.api.get_by_coordinates.assert_called_once_with(('41.85',
                                                             '-87.65'))

        # test zip option
        result = self.runner.invoke(cli, ['weather', '--zip', '60611'])
        self.assertIs(None, result.exception)
        self.assertEqual(0, result.exit_code)
        self.api.get_by_zip.assert_called_once_with('60611')

        # test no options
        result = self.runner.invoke(cli, ['weather'])
        self.assertIsInstance(SystemExit(1), type(result.exception))
        self.assertEqual(1, result.exit_code)
