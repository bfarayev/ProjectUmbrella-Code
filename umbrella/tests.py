from django.test import Client
from umbrella.models import Post
import unittest

class UmbrellaTestCases(unittest.TestCase):
    def test_index(self):
        """Simplest test: Check if homepage is up"""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    #TODO:
    # Adding sample test scenarios:
        # - Create a post with empty content
        # - Create a post with empty category
        # - Create a category
        # - Create a location