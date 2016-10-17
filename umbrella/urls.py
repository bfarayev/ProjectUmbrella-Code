from django.conf.urls import url
from django.http import HttpResponse

from . import views

app_name = "umbrella"


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^$',views.googlemap, name='googlemap',),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^register/', views.register, name='register'),
    url(r'^createSample', views.createSampleData, name='createSampleData'),
    url(r'^createNewPost/', views.createNewPost, name='createNewPost'),
    url(r'^createUser/', views.createUser, name='createUser'),
    url(r'^viewProfile/', views.view_profile, name='view_profile'),
    url(r'^authenticateUser/', views.authenticateUser, name='authenticateUser'),
    url(r'^logout/', views.logoutView, name='logout'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^updateUserProfile/', views.updateUserProfile, name='updateUserProfile'),
    url(r'^updateUserPassword/', views.updateUserPassword, name='updateUserPassword'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
    url(r'^9E356E0335967BC6D12CE4F970AF8C2B.txt', lambda x: HttpResponse("8EE3F2F74363112249C5DC008D51D06828C71503\ncomodoca.com", content_type="text/plain"), name="sslcert"),
    url(r'^updateMarker/', views.updateMarker, name='updateMarker')
]
