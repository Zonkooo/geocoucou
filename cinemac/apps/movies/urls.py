from apps.movies.views import *
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^fichefilm/$', fichefilm, name='fichefilm'),
	url(r'^profil/$', profil, name='profil'),
	url(r'^xd_receiver\.html$', xd_receiver),
	url(r'^creerEvt/$', creerEvt, name='creerEvt'),
	url(r'^evenement/$', evenement, name='evenement'),
	url(r'^listeMembre/$', listeMembre, name='listeMembre'),
	url(r'^resultatRecherche/$', resultatRecherche, name='resultatRecherche'),
)
