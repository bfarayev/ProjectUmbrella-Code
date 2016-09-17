#from django.db import models
# How about following one?
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=40)
    # TODO: Define the list of categories
    # @classmethod
    # def create(cls, category_name, category_description):
    #     _category = cls(title=category_name, description=category_description)
    #     return _category
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

    # @classmethod
    # def create(cls, position):
    #     # Create a post with default location values
    #     _location = Location(latitude=position[0], longitude=position[1])
    #     _location.save()
    #
    #     # Create a category and set it "Uncategorized"
    #     _category = Category()
    #     _category.create("Uncategorized", "Non-description")
    #     _category.save()
    #
    #     # Now create a post
    #     post = Post()
    #     post.location = _location
    #     post.title = "Post title"
    #     post.content = "Sample Post Content"
    #     post.save()

    def __str__(self):
        return str(self.post_title)

