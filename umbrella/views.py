from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
import json
from django.template import defaultfilters

from .models import *


def auto_refresh(request):
    if request.method == 'GET' and request.is_ajax():
        latest_post_list = Post.objects.all().order_by('-timestamp')
        lat = [latest_post.location.latitude for latest_post in latest_post_list]
        lng = [latest_post.location.longitude for latest_post in latest_post_list]
        username = [latest_post.user.username for latest_post in latest_post_list]
        content = [latest_post.content for latest_post in latest_post_list]
        pk = [latest_post.pk for latest_post in latest_post_list]
        image = [str(latest_post.icons) for latest_post in latest_post_list]
        time = [defaultfilters.date(latest_post.timestamp, "P jS N") for latest_post in latest_post_list]
        time_since = [defaultfilters.timesince(latest_post.timestamp) for latest_post in latest_post_list]

        combine_data = json.dumps({'lat': lat, 'lng': lng, 'user': username, 'content': content,
                                   'pk': pk, 'image': image, 'time': time, 'time_since': time_since})
        return HttpResponse(combine_data
                            , content_type="application/json")
    else:
        return render(request, 'umbrella/googlemap.html')


def update_user_profile(request):
    """Method to handle updating the information in the user model"""

    if request.method == 'POST':
        actual_user = request.user

        old_username = actual_user.username
        old_email    = actual_user.email

        actual_user.username = request.POST['display_name']
        actual_user.email = request.POST['email']

        if User.objects.filter(username=actual_user.username).exists() and actual_user.username != old_username:
            messages.add_message(request, messages.ERROR, "That display name is taken already! Try something else.",
                                 "edit")
            return HttpResponseRedirect(reverse('umbrella:googlemap'))

        if User.objects.filter(email=actual_user.email).exists()and actual_user.email != old_email:
            messages.add_message(request, messages.ERROR, "That email address is taken already! Try something else.",
                                 "edit")
            return HttpResponseRedirect(reverse('umbrella:googlemap'))

        actual_user.save()

        pass
        return HttpResponseRedirect(reverse('umbrella:googlemap'))
    else:
        print("This is not a POST request. Can't update user profile now..")
    return render(request, 'umbrella/updateUserProfile.html')


def update_user_password(request):
    if request.method == 'POST':
        actual_user = request.user
        actual_user.set_password(request.POST['new_password'])
        actual_user.save()

        pass
        return HttpResponseRedirect(reverse('umbrella:googlemap'))
    else:
        print("This is not a POST request. Can't update password now..")
    return render(request, 'umbrella/updateUserProfile.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('umbrella:googlemap'))


def is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def authenticate_user(request):
    user_email = request.POST['inputEmail']
    user_pass = request.POST['inputPassword']
    if is_valid_email(user_email):
        try:
            username = User.objects.filter(email=user_email).values_list('username', flat=True)
        except User.DoesNotExist:
            username = None

    kwargs = {'username': username, 'password': user_pass}
    user = authenticate(**kwargs)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('umbrella:googlemap'))
    else:
        messages.add_message(request, messages.ERROR, 'We don\'t know the username or you mistyped the password - Try again, mate!', "signin")
        return HttpResponseRedirect(reverse('umbrella:googlemap'))


def view_profile(request):
    return render(request, 'umbrella/viewProfile.html')


def create_user(request):
    user_name = request.POST['display_name']
    user_pass = request.POST['password']
    user_mail = request.POST['email']

    if User.objects.filter(username=user_name).exists():
        messages.add_message(request, messages.ERROR, "That display name is taken already! Try something else.", "create")
        return HttpResponseRedirect(reverse('umbrella:googlemap'))

    if User.objects.filter(email=user_mail).exists():
        messages.add_message(request, messages.ERROR, "That email address is taken already! Try something else.", "create")
        return HttpResponseRedirect(reverse('umbrella:googlemap'))

    user = User.objects.create_user(user_name,
                                    user_mail,
                                    user_pass
                                    )
    user.save()

    kwargs = {'username': user_name, 'password': user_pass}
    user = authenticate(**kwargs)
    login(request, user)

    return HttpResponseRedirect(reverse('umbrella:googlemap'))


def index(request):
    """Returning index.html"""

    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/index.html', context)


def sign_in(request):
    return render(request, 'umbrella/signin.html')


def register(request):
    return render(request, 'umbrella/register.html')


def googlemap(request):
    """Fetching posts"""

    latest_post_list = Post.objects.all().order_by('-timestamp')
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/googlemap.html', context)


def contact(request):
    return render(request, 'umbrella/contact.html')


def about(request):
    return render(request, 'umbrella/about.html')


def create_new_post(request):
    """Create a new post """

    # Make sure it's a POST request and it is an AJAX
    if request.method == 'POST' and request.is_ajax():
        post_latitude = request.POST['newPostLat']
        pots_longitude = request.POST['newPostLong']
        title = 'Placeholder Title'
        content = request.POST['newPostContent']
        description = 'Placeholder Description'
        location_ = Location(latitude=float(post_latitude), longitude=float(pots_longitude))
        location_.save()
        category_ = Category(title=title, description=description)
        category_.save()
        user = request.user
        icon_name = request.POST['icons_selection']

        # Interpret image value to path
        if icon_name == 'yellow':
            icon = 'static/images/icons/yellow-map-pin-silhouette32x32.png'
        elif icon_name == 'green':
            icon = 'static/images/icons/green-map-pin-silhouette32x32.png'
        elif icon_name == 'purple':
            icon = 'static/images/icons/purple-map-pin-silhouette32x32.png'
        elif icon_name == 'blue':
            icon = 'static/images/icons/blue-map-pin-silhouette32x32.png'
        else:
            icon = 'static/images/icons/map-pin-silhouette32x32.png'

        new_post = Post()
        new_post.icons = icon
        new_post.content = content
        new_post.save()
        new_post.location = location_
        new_post.user = user
        new_post.category.add(category_)
        new_post.save()

        # Resource created
        return HttpResponse(json.dumps({'icon': icon}), content_type="application/json")


def create_sample_data(request):
    """ Add 5 sample user accounts that author some sample posts
    This function populates the database with some sample data
    This comes in handy for demonstrations as well as for manual debugging
    """

    position_1 = [-33.890136, 151.193109]
    title_1 = 'Category A'
    content_1 = "I'm in the PNR building, does anyone have a spare umbrella?"
    description_1 = 'This is Category A'
    icon_1 = 'static/images/icons/blue-map-pin-silhouette32x32.png'
    location_1 = Location(latitude=position_1[0], longitude=position_1[1])
    location_1.save()
    category_1 = Category(title=title_1, description=description_1)
    category_1.save()
    user_1 = User.objects.create_user('louis',
                                      'louis@gmail.com',
                                      '123456'
                                      )
    user_1.save()

    position_2 = [-33.886867, 151.187496]
    title_2 = "Category B"
    content_2 = "Anyone keen for a drink at the bar? That super awesome band everyone likes is playing tonight as well"
    description_2 = 'This is Category B'
    icon_2 = 'static/images/icons/green-map-pin-silhouette32x32.png'
    location_2 = Location(latitude=position_2[0], longitude=position_2[1])
    location_2.save()
    category_2 = Category(title=title_2, description=description_2)
    category_2.save()
    user_2 = User.objects.create_user('aguo',
                                      'austynguo@gmail.com',
                                      'asdf1234'
                                      )
    user_2.save()

    position_3 = [-33.889639, 151.190629]
    title_3 = "Category C"
    content_3 = "Pool competition at 12, meet us at the International Student Lounge!! :)"
    description_3 = 'This is Category C'
    icon_3 = 'static/images/icons/yellow-map-pin-silhouette32x32.png'
    location_3 = Location(latitude=position_3[0], longitude=position_3[1])
    location_3.save()
    category_3 = Category(title=title_3, description=description_3)
    category_3.save()
    user_3 = User.objects.create_user('kai',
                                      'kai@gmail.com',
                                      '123456'
                                      )
    user_3.save()

    position_4 = [-33.887348, 151.191745]
    title_4 = "Category D"
    content_4 = "Come have a kick around with the USyd Social Football Club, 12pm at the park"
    description_4 = "This is Category D"
    icon_4 = 'static/images/icons/purple-map-pin-silhouette32x32.png'
    location_4 = Location(latitude=position_4[0], longitude=position_4[1])
    location_4.save()
    category_4 = Category(title=title_4, description=description_4)
    category_4.save()
    user_4 = User.objects.create_user('bakhtiyar',
                                      'bakhtiyar@gmail.com',
                                      '123456'
                                      )
    user_4.save()

    position_5 = [-33.888373, 151.193440]
    title_5 = "Category E"
    content_5 = "A fun-filled night of entertainment awaits - Catch the Law Revue this Saturday night at the Seymour " \
                "Centre"
    description_5 = "This is Category E"
    icon_5 = 'static/images/icons/map-pin-silhouette32x32.png'
    location_5 = Location(latitude=position_5[0], longitude=position_5[1])
    location_5.save()
    category_5 = Category(title=title_5, description=description_5)
    category_5.save()
    user_5 = User.objects.create_user('alexandru',
                                      'alexandru@gmail.com',
                                      '123456'
                                      )
    user_5.save()

    post_1 = Post()
    post_1.content = content_1
    post_1.save()
    post_1.location = location_1
    post_1.category.add(category_1)
    post_1.user = user_1
    post_1.icons = icon_1
    post_1.save()

    post_2 = Post()
    post_2.content = content_2
    post_2.save()
    post_2.location = location_2
    post_2.category.add(category_2)
    post_2.user = user_2
    post_2.icons = icon_2
    post_2.save()

    post_3 = Post()
    post_3.content = content_3
    post_3.save()
    post_3.location = location_3
    post_3.category.add(category_3)
    post_3.user = user_3
    post_3.icons = icon_3
    post_3.save()

    post_4 = Post()
    post_4.content = content_4
    post_4.save()
    post_4.location = location_4
    post_4.category.add(category_4)
    post_4.user = user_4
    post_4.icons = icon_4
    post_4.save()

    post_5 = Post()
    post_5.content = content_5
    post_5.save()
    post_5.location = location_5
    post_5.category.add(category_5)
    post_5.user = user_5
    post_5.icons = icon_5
    post_5.save()

    return render(request, 'umbrella/googlemap.html')
