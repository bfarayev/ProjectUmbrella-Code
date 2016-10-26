from django.conf.urls import url
from django.http import HttpResponse

from . import views

app_name = "umbrella"

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.googlemap, name='googlemap'),
    url(r'^signin/', views.sign_in, name='signin'),
    url(r'^register/', views.register, name='register'),
    url(r'^createSample', views.create_sample_data, name='createSampleData'),
    url(r'^createNewPost/', views.create_new_post, name='createNewPost'),
    url(r'^createUser/', views.create_user, name='createUser'),
    url(r'^viewProfile/', views.view_profile, name='view_profile'),
    url(r'^authenticateUser/', views.authenticate_user, name='authenticateUser'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^updateUserProfile/', views.update_user_profile, name='updateUserProfile'),
    url(r'^updateUserPassword/', views.update_user_password, name='updateUserPassword'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"),
        name="robots_file"),
    url(r'^9E356E0335967BC6D12CE4F970AF8C2B.txt',
        lambda x: HttpResponse("8EE3F2F74363112249C5DC008D51D06828C71503\ncomodoca.com", content_type="text/plain"),
        name="sslcert")
]
