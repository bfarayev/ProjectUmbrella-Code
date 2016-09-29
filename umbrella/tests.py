import unittest

from django.test import Client
from umbrella.models import Category
from umbrella.models import Location
from umbrella.models import Post, User
from umbrella.views import createNewPost

class UmbrellaTestCases(unittest.TestCase):
    def createUser(self, username, passwd, email):
        """Create a user - normal flow"""
        user = User.objects.create_user(username, email,passwd)
        user.save()

    def test_index(self):
        """Simplest test: Check if homepage is up"""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def testUserExists(self):
        self.createUser("test","Pwd123","me@test.com")
        self.assertIsNotNone(User.objects.get(username = 'test'))

    def testCreateUserWithInvalidParams(self):
        isFailed = False
        try:
            self.createUser("", "Pwd1", "me@test1.com")
        except ValueError:
            isFailed = True

        self.assertTrue(isFailed)

    # Adding sample test scenarios:
        # - Create a post with empty content
        # - Create a post with empty category
        # - Create a category
        # - Create a location