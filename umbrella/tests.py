from django.test import Client
import unittest

class UmbrellaTestCases(unittest.TestCase):
    def test_index(self):
        """Simplest test: Check if homepage is up"""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)