from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    # Uncomment below lines to see the post in Postgres DB
    Post.create()
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/index.html', context)


def signin(request):
    return render(request, 'umbrella/signin.html')


def googlemap(request):
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/googlemap.html',context)
