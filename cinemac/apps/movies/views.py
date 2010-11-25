# Create your views here.
from apps.movies.models import *
from django.shortcuts import render_to_response
from apps.movies.forms import *

def index(request):
	return render_to_response('cinemac/index.html')

	
def fichefilm(request):
	return render_to_response('cinemac/fichefilm.html')

def profil(request):
        form = ProfilForm()
        return render_to_response('cinemac/profil.html',{
                'form':form,
        })
