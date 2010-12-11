#-*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import *

class ProfilForm(forms.Form):
    favouriteFilm = forms.CharField(max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField(required=False)

class FilmForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
	'''PROMO =(
    ('2010/02/02','IMAC 1'),
    ('2011/02/02','IMAC 2'),
    ('2012/02/02','IMAC 3'),
	)'''

	pseudo = forms.CharField(max_length=100)
	email = forms.EmailField()
	#mdp = forms.CharField(max_length=100)
	#promo = forms.CharField(widget=forms.Select(choices=PROMO))
	promo = forms.IntegerField()
#	contrib = forms.CharField(max_length=100)
#	fbmdp = forms.CharField(max_length=100)
#	fbid = forms.IntegerField()

class EventForm(forms.Form):
	'''MOVIETITLE =(
		('megamind','megamind'),
		('megamind','megamind'),
	)'''
	mySlug 			= forms.SlugField(max_length = 255)
	myDate			= forms.DateTimeField()
	myLocation		= forms.CharField(max_length = 255)
	myDescription	= forms.CharField()
	#myMovieTitle 	= forms.CharField(widget=forms.Select(choices=MOVIETITLE))
	myMovieTitle	= forms.CharField(max_length = 255)
	myName			= forms.CharField(max_length = 100)
