from django.conf.urls import url

from . import views

app_name = "umbrella"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^register/', views.register, name='register'),
    url(r'^googlemap/',views.googlemap, name='googlemap'),
    url(r'^createSample', views.createSampleData, name='createSampleData'),
    url(r'^createNewPost/', views.createNewPost, name='createNewPost'),
    url(r'^createUser/', views.createUser, name='createUser'),
    url(r'^viewProfile/', views.view_profile, name='view_profile'),
    url(r'^authenticateUser/', views.authenticateUser, name='authenticateUser'),
    url(r'^logout/', views.logoutView, name='logout'),
    url(r'^updateUserProfile/', views.updateUserProfile, name='updateUserProfile'),
    url(r'^updateUserPassword/', views.updateUserPassword, name='updateUserPassword'),
]
