from django.contrib.auth.models import User
from django.contrib.gis.db import models


# import django
# django.setup()
# from registration.forms import RegistrationForm

# Create Category class
class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=40)

    def __str__(self):
        return self.title


# class UpdateProfile(models.ModelForm):
#    username = models.CharField(required=True)
#    email = models.EmailField(required=True)
#    first_name = models.CharField(required=False)
#    last_name = models.CharField(required=False)

#    class Meta:
#        model = User
#        fields = ('username', 'email', 'first_name', 'last_name')

#    def clean_email(self):
#        username = self.cleaned_data.get('username')
#        email = self.cleaned_data.get('email')

#        if email and User.objects.filter(email=email).exclude(username=username).count():
#            raise models.ValidationError(
#                    'This email address is already in use. Please supply a different email address.')
#        return email

#    def save(self, commit=True):
#        user = super(RegistrationForm, self).save(commit=False)
#        user.email = self.cleaned_data['email']

#        if commit:
#            user.save()

#        return user

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
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return str(self.content[0:10])
