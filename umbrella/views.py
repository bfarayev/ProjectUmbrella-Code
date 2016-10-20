from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def update_user_profile(request):
    """Method to handle updating the information in the user model"""

    if request.method == 'POST':
        actual_user = request.user
        actual_user.username = request.POST['display_name']
        actual_user.email = request.POST['email']
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
        # Redirect to signin.html
        return HttpResponseRedirect(reverse('umbrella:signin'))


def view_profile(request):
    return render(request, 'umbrella/viewProfile.html')


def create_user(request):
    user_name = request.POST['display_name']
    user_pass = request.POST['password']
    user_mail = request.POST['email']

    user = User.objects.create_user(user_name,
                                    user_mail,
                                    user_pass
                                    )
    user.save()
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

        new_post = Post()
        new_post.content = content
        new_post.save()
        new_post.location = location_
        new_post.user = user
        new_post.category.add(category_)
        new_post.save()

        # Resource created
        return HttpResponse(status=201)


def create_sample_data(request):
    """ Add 5 sample user accounts that author some sample posts
    This function populates the database with some sample data
    This comes in handy for demonstrations as well as for manual debugging
    """

    position_1 = [-33.890136, 151.193109]
    title_1 = 'Category A'
    content_1 = "I'm in the PNR building, does anyone have a spare umbrella?"
    description_1 = 'This is Category A'
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
    post_1.save()

    post_2 = Post()
    post_2.content = content_2
    post_2.save()
    post_2.location = location_2
    post_2.category.add(category_2)
    post_2.user = user_2
    post_2.save()

    post_3 = Post()
    post_3.content = content_3
    post_3.save()
    post_3.location = location_3
    post_3.category.add(category_3)
    post_3.user = user_3
    post_3.save()

    post_4 = Post()
    post_4.content = content_4
    post_4.save()
    post_4.location = location_4
    post_4.category.add(category_4)
    post_4.user = user_4
    post_4.save()

    post_5 = Post()
    post_5.content = content_5
    post_5.save()
    post_5.location = location_5
    post_5.category.add(category_5)
    post_5.user = user_5
    post_5.save()

    return render(request, 'umbrella/googlemap.html')
