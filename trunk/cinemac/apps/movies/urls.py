#-*- coding: utf-8 -*-
from apps.movies.views import *
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^fichefilm/$', fichefilm, name='fichefilm'),
	url(r'^profil/$', profil, name='profil'),
	url(r'^login/$', login, name='login'),
	url(r'^xd_receiver\.html$', xd_receiver),
	url(r'^creerEvt/$', creerEvt, name='creerEvt'),
	url(r'^evenement/$', evenement, name='evenement'),
	url(r'^listeMembre/$', listeMembre, name='listeMembre'),
	url(r'^listeFilms/$', listeFilms, name='listeFilms'),
	url(r'^listeEvt/$', listeEvt, name='listeEvt'),
	url(r'^listeMesInvit/$', listeMesInvit, name='listeMesInvit'),
	url(r'^resultatRecherche/$', resultatRecherche, name='resultatRecherche'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^mentionsLegales/$', mentionsLegales, name='mentionsLegales'),
	url(r'^top10/$', top10, name='top10'),
)

handler404 = '^error_404/$'