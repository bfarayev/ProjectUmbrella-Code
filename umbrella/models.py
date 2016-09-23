#from django.db import models
# FIXME: How about following one?
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



# Create Category class
class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=40)
    # TODO: Define the list of categories

    def __str__(self):
        return self.title

# Create Location class
class Location(models.Model):
    latitude = models.FloatField(default=-33.888584)
    longitude = models.FloatField(default=151.1851586)

    def __str__(self):
        return str([self.latitude, self.longitude])

# Create the Posts class
class Post(models.Model):

    content = models.TextField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return str(self.content[0:10])



