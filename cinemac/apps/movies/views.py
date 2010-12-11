#-*- coding: utf-8 -*-
# Create your views here.
from apps.movies.models import *
from django.shortcuts import render_to_response
from apps.movies.forms import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.template import RequestContext
from django.core.mail import send_mail



def index(request):
		event = Event.objects.order_by('-date')[:2]
		members  = Member.objects.order_by('-date_joined')[:2] #- pour l'ordre décroissant
		val= {"members" :members, "event" :event,}
		return render_to_response('cinemac/index.html',val)

def fichefilm(request):
	if (request.method == 'GET'):
		try:
			movie_id = request.GET['mid']
			myMovie = Movie.objects.get(id = movie_id)

			return render_to_response('cinemac/fichefilm.html', {'movie':myMovie,}, context_instance = RequestContext(request) )
		except:
			return render_to_response('cinemac/404.html')
	return render_to_response('cinemac/404.html')
	
		
def profil(request):
	if (request.method == 'GET'):
		try:
			m = Member.objects.get(id = request.GET['uid'])
			val = {
					"member"	: m,
				  }
			return render_to_response('cinemac/profil.html', val, context_instance = RequestContext(request) )
		except:
			return render_to_response('cinemac/404.html')
	elif request.user.is_authenticated():
		m = Member.objects.get(contrib_user = request.user)
		val = {
				"member"	: m,
			  }
		return render_to_response('cinemac/profil.html', val, context_instance = RequestContext(request) )
	else:
		return render_to_response('cinemac/404.html')
	
def xd_receiver(request): #facebook
    return render_to_response('xd_receiver.html')
    
def creerEvt(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			mySlug = form.cleaned_data['mySlug']
			myDate = form.cleaned_data['myDate']
			myLocation = form.cleaned_data['myLocation']
			myDescription = form.cleaned_data['myDescription']
			myMovieTitle = form.cleaned_data['myMovieTitle']
			myName = form.cleaned_data['myName']
			myPseudo = Member.objects.get(pseudo = myName)
			myMovie = Movie.objects.get(title = myMovieTitle)
			#Creation dun objet du type de la table voulue
			#Passage par parametre TABLE_VOULUE(nom_attribut_table=.., nom_attribut_table=..)
			myEvent = Event(slug=mySlug,date=myDate,location=myLocation,description=myDescription, movie=myMovie, creator=myPseudo)
			#Enregistrement dans la Base De Donnees avec monObjet.save()
			myEvent.save()
			return HttpResponseRedirect('#')
	else:
		form = EventForm()
			
	return render_to_response('cinemac/creerEvt.html',{
		'form':form,
	}, context_instance=RequestContext(request))
	
def evenement(request):
	if (request.method == 'GET'):
		try:
			event_id = request.GET['mid']
			myEvent = Event.objects.get(id = event_id )

			return render_to_response('cinemac/evenement.html', {'event':myEvent,}, context_instance = RequestContext(request) )
		except:
			return render_to_response('cinemac/404.html')
	return render_to_response('cinemac/404.html')

def top10(request):
	if (request.method == 'GET'):
            try:
                movies  = Movie.objects.order_by('-rating_imdb')[:10]
            except:
                movies  = Movie.objects.order_by('id')
        else:
            movies  = Movie.objects.order_by('id')
	
	val= {"movies" :movies,}
	return render_to_response('cinemac/top10.html', val, context_instance = RequestContext(request) )

@csrf_exempt
#todo : revoir la recherche et tester si elle fonctionne bien
def resultatRecherche(request):
	if request.method == 'POST':
		try:
			q = request.POST['content']
		
			clause = Q(pseudo__icontains=q)			   
			members = Member.objects.filter(clause).distinct()
			clause = Q(name__icontains=q) | Q(forename__icontains=q)
			artists = Artist.objects.filter(clause).distinct()
			clause = Q(title__icontains=q)
			films = Movie.objects.filter(clause).distinct()
		except:
			return render_to_response('cinemac/404.html')
	
	else :
		members = Member.objects.distinct()
		artists = None;
		films = None;
	
	return render_to_response('cinemac/resultatRecherche.html',{
		'members_list' : members,
		'artists_list' : artists,
		'films_list' : films,
	})
	
def mentionsLegales(request):
	return render_to_response('cinemac/mentionsLegales.html')	

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			#recipients = ['cmellany91@gmail.com']
			recipients = ['projetwebimac@googlegroups.com']
			send_mail(subject, message, sender, recipients)
			return render_to_response('cinemac/thanks.html')

			return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('cinemac/contact.html', {'form': form, 'form_action': "/contact/"}, context_instance=RequestContext(request))

	
def listeEvt(request):
	if (request.method == 'GET'):
            try:
                events  = Event.objects.order_by( request.GET['mode'])
            except:
                events  = Event.objects.order_by('id')
        else:
            events  = Event.objects.order_by('id')
	
	val= {"event" :events,}
	return render_to_response('cinemac/listeEvt.html', val, context_instance = RequestContext(request) )


def listeMembre(request):

	if (request.method == 'GET') & ('mode' in request.GET > 0):
            try:
                members  = Member.objects.order_by( request.GET['mode'])
            except:
                members  = Member.objects.order_by('date_joined')
        else:
            members  = Member.objects.order_by('date_joined')
        val= {"members" :members,}

	return render_to_response('cinemac/listeMembre.html', val, context_instance = RequestContext(request) )

def listeFilms(request):
        if (request.method == 'GET'):
            try:
                movies  = Movie.objects.order_by( request.GET['mode'])
            except:
                movies  = Movie.objects.order_by('id')
        else:
            movies  = Movie.objects.order_by('id')
	
	val= {"movie" :movies,}
	return render_to_response('cinemac/listeFilms.html', val, context_instance = RequestContext(request) )
	
	
def listeMesInvit(request):
	evenement  = Event.objects.order_by('date')
	val= {"evenement" :evenement,}
	return render_to_response('cinemac/listeMesInvit.html', val, context_instance = RequestContext(request) )
	
def login(request):
	try:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				pseudo = form.cleaned_data['pseudo']
				email = form.cleaned_data['email']
				promo = form.cleaned_data['promo']
			
				m = Member.objects.get(contrib_user = request.user)
				#remplissage des infos manquantes
				m.pseudo = pseudo
				m.mail = email
				m.class_year = "%d-01-01" % promo
				m.save()
				return HttpResponseRedirect('/')
		else:
			m = Member.objects.get(contrib_user = request.user)
			form = LoginForm(initial={"pseudo" : m.pseudo, "email" : m.mail, "promo" : m.class_year.year, })
		
		return render_to_response('cinemac/login.html',{'form':form,}, context_instance = RequestContext(request))
	except:
		return HttpResponseRedirect('/')	
