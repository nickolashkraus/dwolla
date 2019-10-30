import logging
from unittest.mock import patch

from click.testing import CliRunner

from ..cli import cli
from .base import BaseTestCase


class CliTestCase(BaseTestCase):
    def setUp(self):
        super(CliTestCase, self).setUp()
        self.runner = CliRunner()

    def test_cli_version(self):
        result = self.runner.invoke(cli, ['--version'])
        self.assertIs(None, result.exception)
        self.assertEqual(0, result.exit_code)
        self.assertEqual('Dwolla 1.0.1\n', result.output)

    def test_cli_no_subcommand(self):
        result = self.runner.invoke(cli)
        self.assertIsInstance(SystemExit(1), type(result.exception))
        self.assertEqual(1, result.exit_code)
        self.assertIn('Usage', result.output)

    def test_configure_logging_exception(self):
        self.get_logger = patch.object(logging, 'getLogger').start()
        self.get_logger.return_value.addHandler.side_effect = Exception
        result = self.runner.invoke(cli, [])
        self.assertIsInstance(result.exception, Exception)
        self.assertEqual(1, result.exit_code)
