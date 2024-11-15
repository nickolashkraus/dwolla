import logging
import unittest
from unittest.mock import patch


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.addCleanup(patch.stopall)
        self.logging_info = patch.object(logging, 'info').start()
