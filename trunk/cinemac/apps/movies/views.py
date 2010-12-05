# Create your views here.
from apps.movies.models import *
from django.shortcuts import render_to_response
from apps.movies.forms import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.template import RequestContext

def index(request):
	return render_to_response('cinemac/index.html')

def fichefilm(request):
	if request.method == 'GET':
		movie_id = int(request.GET['mid'])
		movie = Movie.objects.get(id = movie_id)
		
		#bricolage a corriger avec du code dans le html
		dir_string = ""
		act_string = ""
		genre_string = ""
		for d in movie.directed_by.all():
			dir_string += d.__unicode__() + ", "
		for a in movie.played_by.all():
			act_string += a.__unicode__() + ", "
		for g in movie.genre_is.all():
			genre_string += g.__unicode__() + ", "
		
		val = {
				"title"		: movie.title,
				"directors"	: dir_string,
				"actors"	: act_string,
				"genres"	: genre_string,
				"year"		: movie.year.year,
				"country"	: movie.country,
				"synopsis"	: movie.synopsis,
			  }
		return render_to_response('cinemac/fichefilm.html', val, context_instance = RequestContext(request) )
	else:
		return render_to_response('cinemac/fichefilm.html')

def profil(request):
	if request.method == 'POST':
		form = ProfilForm(request.POST)
		if form.is_valid():
			favouriteFilm = form.cleaned_data['favouriteFilm']
			#Creation dun objet du type de la table voulue
			#Passage par parametre TABLE_VOULUE(nom_attribut_table=.., nom_attribut_table=..)
			monFilmFavori = Genre(name=favouriteFilm)
			#Enregistrement dans la Base De Donnees avec monObjet.save()
			monFilmFavori.save()
			return HttpResponseRedirect('#') # Redirect after POST
	else:
		form = ProfilForm()
				
	return render_to_response('cinemac/profil.html',{
		'form':form,
	})
	
def login(request):
	form = LoginForm()
	return render_to_response('cinemac/login.html',{
		'form':form,
	})
	
def creerEvt(request):
	return render_to_response('cinemac/creerEvt.html')
	
def evenement(request):
	return render_to_response('cinemac/evenement.html')

def listeMembre(request):
	return render_to_response('cinemac/listeMembre.html')

@csrf_exempt
#todo : revoir la recherche et tester si elle fonctionne bien
def resultatRecherche(request):
	q = request.POST['content']
	
	clause = Q(slug__icontains=q)			   
	members = Member.objects.filter(clause).distinct()
	artists = Artist.objects.filter(clause).distinct()
	films = Movie.objects.filter(clause).distinct()
		
	return render_to_response('cinemac/resultatRecherche.html',{
	'members_list' : members,
	'artists_list' : artists,
	'films_list' : films
	})
	
		

Artist
