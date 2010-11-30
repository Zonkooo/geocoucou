# Create your views here.
from apps.movies.models import *
from django.shortcuts import render_to_response
from apps.movies.forms import *

def index(request):
	return render_to_response('cinemac/index.html')

def fichefilm(request):
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
					#return HttpResponseRedirect('#') # Redirect after POST
        else:
                form = ProfilForm()

       return render_to_response('cinemac/profil.html',{
                'form':form,
        })
        

