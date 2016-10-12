from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *



def updateUserPassword(request):
    if request.method == 'POST':
        actual_user = request.user
        actual_user.set_password(request.POST['password'])
        actual_user.save()

        #TODO: once the profile has been updated, return the user to the voiew profile page
        pass
        return HttpResponseRedirect(reverse('umbrella:index'))
    else:
        print("this has to be here to work I do not know why = might be my logic")
    return render(request, 'umbrella/updateUserProfile.html')



# procedure to handle updating the information in the user model
def updateUserProfile(request):
    if request.method == 'POST':
        actual_user = request.user
        actual_user.username = request.POST['display_name']
        actual_user.email = request.POST['email']
        actual_user.save()

        #TODO: once the profile has been updated, return the user to the voiew profile page
        pass
        return HttpResponseRedirect(reverse('umbrella:index'))
    else:
        print("this has to be here to work I do not know why = might be my logic")
    return render(request, 'umbrella/updateUserProfile.html')


# TODO: Log out
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('umbrella:index'))


# TODO: Authenticating users
def _is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def authenticateUser(request):
    userEmail = request.POST['inputEmail']
    userPass = request.POST['inputPassword']
    if _is_valid_email(userEmail):
        try:
            username = User.objects.filter(email=userEmail).values_list('username', flat=True)
        except User.DoesNotExist:
            username = None

    kwargs = {'username': username, 'password': userPass}
    user = authenticate(**kwargs)

    if user is not None:
        login(request, user)
        # Redirect to userProfile for testing
        return HttpResponseRedirect(reverse('umbrella:index'))
    else:
        # Redirect to signin.html
        return HttpResponseRedirect(reverse('umbrella:signin'))


def view_profile(request):
    return render(request, 'umbrella/viewProfile.html')


def createUser(request):
    userName = request.POST['display_name']
    userPass = request.POST['password']
    userMail = request.POST['email']
    # TODO: add first_name and last_name into User
    userFirstName = request.POST['first_name']
    userLastName= request.POST['last_name']

    user = User.objects.create_user(userName,
                             userMail,
                             userPass
                             )
    user.save()
    return HttpResponseRedirect(reverse('umbrella:index'))


def index(request):
    latest_post_list = Post.objects.all()
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/index.html', context)


def signin(request):
    return render(request, 'umbrella/signin.html')


def register(request):
    return render(request, 'umbrella/register.html')


def googlemap(request):
    latest_post_list = Post.objects.all().order_by('-timestamp')
    context = {'post_list': latest_post_list}
    return render(request, 'umbrella/googlemap.html',context)

def createNewPost(request):
    postLatitude = request.POST['newPostLat']
    potsLongitude = request.POST['newPostLong']
    title = 'Placeholder Title'
    content = request.POST['newPostContent']
    description = 'Placeholder Description'
    _location_ = Location(latitude=float(postLatitude), longitude=float(potsLongitude))
    _location_.save() # what does .save() do?
    _category_ = Category(title=title, description=description)
    _category_.save()
    _user_ = request.user

    newPost = Post()
    newPost.content = content
    newPost.save()
    newPost.location = _location_
    newPost.user = _user_
    newPost.category.add(_category_)
    newPost.save()

    return HttpResponseRedirect(reverse('umbrella:googlemap'))


def createSampleData(request):
    # TODO: Add a few sample user accounts that author some sample posts
    # This function populates the database with some sample data
    # This comes in handy for demonstrations as well as for manual debugging
    position_1 = [-33.890136, 151.193109]
    title_1 = 'Category A'
    content_1 = "I'm in the PNR building, does anyone have a spare umbrella?"
    descrip_1 = 'This is Category A'
    _location_1 = Location(latitude=position_1[0], longitude=position_1[1])
    _location_1.save()
    _category_1 = Category(title=title_1, description=descrip_1)
    _category_1.save()
    user_1 = User.objects.create_user('louis',
                                      'louis@gmail.com',
                                      '123456'
                                      )
    user_1.save()

    position_2 = [-33.886867, 151.187496]
    title_2 = "Category B"
    content_2 = "Anyone keen for a drink at the bar? That super awesome band everyone likes is playing tonight as well"
    descrip_2 = 'This is Category B'
    _location_2 = Location(latitude=position_2[0], longitude=position_2[1])
    _location_2.save()
    _category_2 = Category(title=title_2, description=descrip_2)
    _category_2.save()
    user_2 = User.objects.create_user('aguo',
                                      'austynguo@gmail.com',
                                      'asdf1234'
                                      )
    user_2.save()

    position_3 = [-33.889639, 151.190629]
    title_3 = "Category C"
    content_3 = "Pool competition at 12, meet us at the International Student Lounge!! :)"
    descrip_3 = 'This is Category C'
    _location_3 = Location(latitude=position_3[0], longitude=position_3[1])
    _location_3.save()
    _category_3 = Category(title=title_3, description=descrip_3)
    _category_3.save()
    user_3 = User.objects.create_user('kai',
                                      'kai@gmail.com',
                                      '123456'
                                      )
    user_3.save()

    position_4 = [-33.887348, 151.191745]
    title_4 = "Category D"
    content_4 = "Come have a kick around with the USyd Social Football Club, 12pm at the park"
    descrip_4 = "This is Category D"
    _location_4 = Location(latitude=position_4[0], longitude=position_4[1])
    _location_4.save()
    _category_4 = Category(title=title_4, description=descrip_4)
    _category_4.save()
    user_4 = User.objects.create_user('bakhtiyar',
                                      'bakhtiyar@gmail.com',
                                      '123456'
                                      )
    user_4.save()

    position_5 = [-33.888373, 151.193440]
    title_5 = "Category E"
    content_5 = "A fun-filled night of entertainment awaits - Catch the Law Revue this Saturday night at the Seymour Centre"
    descrip_5 = "This is Category E"
    _location_5 = Location(latitude=position_5[0], longitude=position_5[1])
    _location_5.save()
    _category_5 = Category(title=title_5, description=descrip_5)
    _category_5.save()
    user_5 = User.objects.create_user('alexandru',
                                      'alexandru@gmail.com',
                                      '123456'
                                      )
    user_5.save()

    post_1 = Post()
    post_1.content = content_1
    post_1.save()
    post_1.location = _location_1
    post_1.category.add(_category_1)
    post_1.user = user_1
    post_1.save()

    post_2 = Post()
    post_2.content = content_2
    post_2.save()
    post_2.location = _location_2
    post_2.category.add(_category_2)
    post_2.user = user_2
    post_2.save()

    post_3 = Post()
    post_3.content = content_3
    post_3.save()
    post_3.location = _location_3
    post_3.category.add(_category_3)
    post_3.user = user_3
    post_3.save()

    post_4 = Post()
    post_4.content = content_4
    post_4.save()
    post_4.location = _location_4
    post_4.category.add(_category_4)
    post_4.user = user_4
    post_4.save()

    post_5 = Post()
    post_5.content = content_5
    post_5.save()
    post_5.location = _location_5
    post_5.category.add(_category_5)
    post_5.user = user_5
    post_5.save()

    return render(request, 'umbrella/index.html')

