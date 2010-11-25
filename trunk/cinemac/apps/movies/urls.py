from apps.movies.views import *
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^films/$', fichefilm, name='fichefilm'),
    url(r'^profil/$', profil, name='profil'),
)