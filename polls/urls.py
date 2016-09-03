from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # how to makes this urls work?-----
    url(r'^postQuestion/$', views.postQuestion.as_view(), name='postQuestion'),
    url(r'^postQuestion/postQ/$', views.postQ, name='postQ'),
    #----------------------------------
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/virtualvote/$', views.virtualvote, name='virtualvote'),
    url(r'^(?P<question_id>[0-9]+)/google/$', views.google, name = 'google'),
]