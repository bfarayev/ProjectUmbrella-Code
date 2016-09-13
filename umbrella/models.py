from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=20)

    # TODO: Define the list of categories
    @classmethod
    def create(cls, category_name):
        _category = cls(title=category_name)
        return _category

# Create Location class
class Location(models.Model):
    latitude = models.FloatField(default=-33.888584)
    longitude = models.FloatField(default=151.1851586)

# Create the Posts class
class Post(models.Model):
    content = models.TextField(max_length=40)
    category = models.ForeignKey(Category, null=True, blank=True)
    location = models.ForeignKey(Location, null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @classmethod
    def create(cls):
        # Create a post with default location values
        _location = Location()
        _location.save()

        # Create a category and set it "Uncategorized"
        _category = Category
        _category.create("Uncategorized")
        -_category.save()

        # Now create a post
        post = Post()
        post.location = _location
        post.content = "Sample Post Content"
        post.save()