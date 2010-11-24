# Create your views here.
from apps.movies.models import *
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('cinemac/index.html')
