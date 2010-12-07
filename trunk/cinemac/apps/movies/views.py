#-*- coding: utf-8 -*-

# Create your views here.
from django.core.mail import send_mail
from apps.movies.models import *
from django.shortcuts import render_to_response
from apps.movies.forms import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.template import RequestContext



def index(request):
        members  = Member.objects.order_by('-date_joined')[:2];
	return render_to_response('cinemac/index.html',members)

def fichefilm(request):
	if (request.method == 'GET') & (len(request.GET.getlist('mid')) > 0):
		movie_id = request.GET['mid']
		movie = Movie.objects.get(id = movie_id)
		
#		imac_r = Rate.objects.filter();#TODO
		note_imac = 0
#		if len(imac_r) != 0:
#			for r in imac_r:
#				note_imac += r.value
#			note_imac /= len(imac_r)
		
		val = {
				"request_ok": True,
				"title"		: movie.title,
				"directors"	: movie.directed_by.all(),
				"actors"	: movie.played_by.all(),
				"genres"	: movie.genre_is.all(),
				"year"		: movie.year.year,
				"country"	: movie.country,
				"synopsis"	: movie.synopsis,
				#non utilises pour l'instant :
				"note_imdb"	: movie.rating_imdb,
				"note_imac"	: note_imac,
				"cover"		: movie.cover,
			  } #TODO : cours, commentaires
	else:
		val = { "request_ok": False, }
	return render_to_response('cinemac/fichefilm.html', val, context_instance = RequestContext(request) )
	
def profil(request):
	return render_to_response('cinemac/profil.html')
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
	
def xd_receiver(request): #facebook
    return render_to_response('xd_receiver.html')
    
def creerEvt(request):
	return render_to_response('cinemac/creerEvt.html')
	
def evenement(request):
	return render_to_response('cinemac/evenement.html')

def listeMembre(request):
	return render_to_response('cinemac/listeMembre.html')

def listeFilms(request):
	return render_to_response('cinemac/listeFilms.html')
	
@csrf_exempt
#todo : revoir la recherche et tester si elle fonctionne bien
def resultatRecherche(request):
	if request.method == 'POST':
		q = request.POST['content']
		
		clause = Q(pseudo__icontains=q)			   
		members = Member.objects.filter(clause).distinct()
		clause = Q(name__icontains=q) | Q(forename__icontains=q)
		artists = Artist.objects.filter(clause).distinct()
		clause = Q(title__icontains=q)
		films = Movie.objects.filter(clause).distinct()
	
	else :
		members = Member.objects.distinct()
		artists = None;
		films = None;
	
	return render_to_response('cinemac/resultatRecherche.html',{
	'members_list' : members,
	'artists_list' : artists,
	'films_list' : films
	})
	
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			recipients = ['cmellany@orange.fr']
			
			send_mail(subject, message, sender, recipients)

			return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('cinemac/contact.html', {'form': form, 'form_action': "/contact/"}, context_instance=RequestContext(request))

def mentionsLegales(request):
	return render_to_response('cinemac/mentionsLegales.html')	
	
#Artist
