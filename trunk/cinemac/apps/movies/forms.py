#-*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import *

class ProfilForm(forms.Form):
    favouriteFilm = forms.CharField(max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField(required=False)

