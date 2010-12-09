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
		# movie = Movie.objects.order_by('date_joined')
		# val={"movie" :movie,}
		members  = Member.objects.order_by('date_joined')[:2]
		val= {"members" :members,}
		return render_to_response('cinemac/index.html',val)

def fichefilm(request):
	if (request.method == 'GET') & ('mid' in request.GET):
		myMovie = Movie.objects.get(id = request.GET['mid']) #ici pb si on met de la merde en param GET
		coursecomment = CourseComment.objects.filter(movie = myMovie)
		
		
#		imac_r = Rate.objects.filter();#TODO
		note_imac = 0
#		if len(imac_r) != 0:
#			for r in imac_r:
#				note_imac += r.value
#			note_imac /= len(imac_r)
		
		val = {
				"request_ok": True,
				"movie"		: myMovie,
				"directors"	: myMovie.directed_by.all(),
				"actors"	: myMovie.played_by.all(),
				"genres"	: myMovie.genre_is.all(),
				#non utilises pour l'instant :
				"note_imac"	: note_imac,
				"coursecomment"	: coursecomment,
			  } #TODO : cours, commentaires
	else:
		val = { "request_ok": False, }
		
	
	return render_to_response('cinemac/fichefilm.html', val, context_instance = RequestContext(request) )
	
def profil(request):
	if (request.method == 'GET') & ('uid' in request.GET) :
		m = Member.objects.get(id = request.GET['uid'])
		val = {
				"logged"	: True,
				"member"	: m,
			  }
	elif request.user.is_authenticated():
		m = Member.objects.get(contrib_user = request.user)
		val = {
				"logged"	: True,
				"member"	: m,
			  }
	else:
		val = { "logged" : False, }
	return render_to_response('cinemac/profil.html', val, context_instance = RequestContext(request) )
	
def xd_receiver(request): #facebook
    return render_to_response('xd_receiver.html')
    
def creerEvt(request):
	return render_to_response('cinemac/creerEvt.html')
	
def evenement(request):
	return render_to_response('cinemac/evenement.html')

def listeMembre(request):

        if (request.method == 'GET') & ('mode' in request.GET > 0):
            try:
                members  = Member.objects.order_by( movie_id = request.GET['mode'])
            except:
                members  = Member.objects.order_by('date_joined')
        else:
            members  = Member.objects.order_by('date_joined')
        val= {"members" :members,}

	return render_to_response('cinemac/listeMembre.html', val, context_instance = RequestContext(request) )

def listeFilms(request):
        if (request.method == 'GET') & (len(request.GET.getlist('mode')) > 0):
                try:
                    members  = Member.objects.order_by( movie_id = request.GET['mode'])
                except:
                    members  = Member.objects.order_by('id')
            else:
                members  = Member.objects.order_by('id')
            val= {"members" :members,}

	movie  = Movie.objects.order_by('id')
	val= {"movie" :movie,}
	return render_to_response('cinemac/listeFilms.html', val, context_instance = RequestContext(request) )
	
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
	evenement  = Event.objects.order_by('date')
	val= {"evenement" : evenement,}
	return render_to_response('cinemac/listeEvt.html', val, context_instance = RequestContext(request) )

def listeMesInvit(request):
	evenement  = Event.objects.order_by('date')
	val= {"evenement" :evenement,}
	return render_to_response('cinemac/listeMesInvit.html', val, context_instance = RequestContext(request) )
