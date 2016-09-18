from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/index.html', context)


def signin(request):
    return render(request, 'umbrella/signin.html')


def googlemap(request):
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/googlemap.html',context)


def createFivePosts(request):
    # TODO: for testing google-map-implementation, delete this and related url in urls.py when complete.
    position_1 = [-33.888584, 151.1851586]
    title_1 = 'Category A'
    content_1 = "I'm in the PNR building, does anyone have a umbrella, HELP me!!!!"
    descrip_1 = 'This is Category A'
    _location_1 = Location(latitude=position_1[0], longitude=position_1[1])
    _location_1.save()
    _category_1 = Category(title=title_1, description=descrip_1)
    _category_1.save()

    position_2 = [-33.888584, 151.2851586]
    title_2 = "Category B"
    content_2 = "I'm so hungry, does anyone can share me a pancake?..." \
                "blah la bhla bhal bh al bha lb hal bh al bh al bha lhb"
    descrip_2 = 'This is Category B'
    _location_2 = Location(latitude=position_2[0], longitude=position_2[1])
    _location_2.save()
    _category_2 = Category(title=title_2, description=descrip_2)
    _category_2.save()

    position_3 = [-33.888584, 151.0851586]
    title_3 = "Category C"
    content_3 = "Amazing competition with your friends! hands up and join us!! :)"
    descrip_3 = 'This is Category C'
    _location_3 = Location(latitude=position_3[0], longitude=position_3[1])
    _location_3.save()
    _category_3 = Category(title=title_3, description=descrip_3)
    _category_3.save()

    position_4 = [-33.788584, 151.1851586]
    title_4 = "Category D"
    content_4 = "I just want to have a long content to test thee..." \
                "text feild 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    descrip_4 = "This is Category D"
    _location_4 = Location(latitude=position_4[0], longitude=position_4[1])
    _location_4.save()
    _category_4 = Category(title=title_4, description=descrip_4)
    _category_4.save()

    position_5 = [-33.988584, 151.1851586]
    title_5 = "Category E"
    content_5 = "Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~AhhAhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh~~~"
    descrip_5 = "This is Category E"
    _location_5 = Location(latitude=position_5[0], longitude=position_5[1])
    _location_5.save()
    _category_5 = Category(title=title_5, description=descrip_5)
    _category_5.save()

    post_1 = Post()
    post_1.content = content_1
    post_1.save()
    post_1.location = _location_1
    post_1.category.add(_category_1)
    post_1.save()

    post_2 = Post()
    post_2.content = content_2
    post_2.save()
    post_2.location = _location_2
    post_2.category.add(_category_2)
    post_2.save()

    post_3 = Post()
    post_3.content = content_3
    post_3.save()
    post_3.location = _location_3
    post_3.category.add(_category_3)
    post_3.save()

    post_4 = Post()
    post_4.content = content_4
    post_4.save()
    post_4.location = _location_4
    post_4.category.add(_category_4)
    post_4.save()

    post_5 = Post()
    post_5.content = content_5
    post_5.save()
    post_5.location = _location_5
    post_5.category.add(_category_5)
    post_5.save()

    return render(request, 'umbrella/index.html')
