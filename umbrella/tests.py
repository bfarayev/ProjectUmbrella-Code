import unittest

from django.test import Client

from umbrella.models import Location
from umbrella.models import User


class UmbrellaTestCases(unittest.TestCase):
    def createUser(self, username, passwd, email):
        """Create a user"""
        user = User.objects.create_user(username, email,passwd)
        user.save()

    def createLocation(self, lat, lon):
        """Create a location"""

        # validation
        if -200 < lat < 200 and -200 < lon < 200:
            loc = Location(latitude=lat, longitude=lon)
            loc.save()
        else:
            raise ValueError('out of boundaries')

    def test_index(self):
        """Simplest test: Check if homepage is up"""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def testCreateUser(self):
        self.createUser("test","Pwd123","me@test.com")
        self.assertIsNotNone(User.objects.get(username = 'test'))

    def testCreateUserWithInvalidParams(self):
        isFailed = False
        try:
            self.createUser("", "Pwd1", "me@test1.com")
        except ValueError:
            isFailed = True

        self.assertTrue(isFailed)

    def testCreateLocation(self):
        self.createLocation(100, 50)
        self.assertIsNotNone(Location.objects.get(latitude=100))

    def testCreateLocationWithInvalidValues(self):
        isFailed = False
        try:
            self.createLocation(500, 1000) # boundary overflow
        except ValueError:
            isFailed = True

        self.assertTrue(isFailed)