from django.conf.urls import url

from . import views

app_name = "umbrella"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^register/', views.register, name='register'),
    url(r'^googlemap/',views.googlemap,name='googlemap'),
    url(r'^createposts/', views.createFivePosts, name='createFivePosts')
]
