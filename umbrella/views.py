from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # Uncomment below lines to see the post in Postgres DB
    # post = Post()
    # post.create()

    return render(request, 'umbrella/index.html')

def signin(request):
    return render(request, 'umbrella/signin.html')

def googlemap(request):
    return render(request, 'umbrella/googlemap.html')
