from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Categories'

    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=50)
    description = models.TextField()


class Post(models.Model):
    def __str__(self):
        return self.subject
    subject = models.CharField(max_length=255)
    content = models.TextField()
    is_public = models.BooleanField()
    data_posted = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    users = models.ManyToManyField(User)
