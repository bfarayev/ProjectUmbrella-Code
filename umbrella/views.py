from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # Create multiple position for testing!!:
    # position_1 = [-33.888584, 151.1851586]
    # position_2 = [-32.888584, 151.1851586]
    # position_3 = [-31.888584, 151.1851586]
    # position_4 = [-30.888584, 151.1851586]
    # position_5 = [-34.888584, 151.1851586]
    # Post.create(position_1)
    # Post.create(position_2)
    # Post.create(position_3)
    # Post.create(position_4)
    # Post.create(position_5)
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/index.html', context)


def signin(request):
    return render(request, 'umbrella/signin.html')


def googlemap(request):
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/googlemap.html',context)
