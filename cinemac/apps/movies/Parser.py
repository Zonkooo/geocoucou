import xml.dom.minidom #for allocine
import json #for imdb
import urllib2
from models import Movie, Genre, Artist

REA_CODE = 8002
ACT_CODE = 8001

class MovieParser:
	#fields from allocine
	title = ""
	title_en = ""
	year = 0
	country = ""
	synopsis = ""
	actors = list()
	directors = list()
	cover = ""
	
	#fields from imdb
	id_imdb = 0
	rating = 0.0
	genres = list()
	
	#other fields
	#slug
	#cover
	
	def __init__(self, id_allocine):
		url = "http://api.allocine.fr/xml/movie?partner=1&code=" + id_allocine
		xml_content = urllib2.build_opener().open(url).read()
		self.parse_allocine_xml(xml_content)
		
		url = "http://www.deanclatworthy.com/imdb/?q=" + self.title_en.replace(' ', '+')
		imdb_content = urllib2.build_opener().open(url).read()
		self.parse_imdb(imdb_content)
		
	def parse_allocine_xml(self, xml_content):
		f = xml.dom.minidom.parseString(xml_content)
		e = f.getElementsByTagName("movie")[0] #the global element containing everyting
		self.title		= e.getElementsByTagName("title")[0].childNodes[0].nodeValue
		self.title_en	= e.getElementsByTagName("originalTitle")[0].childNodes[0].nodeValue
		self.year		= e.getElementsByTagName("productionYear")[0].childNodes[0].nodeValue
		countrylist		= e.getElementsByTagName("nationalityList")[0]
		self.country	= countrylist.getElementsByTagName("nationality")[0].childNodes[0].nodeValue
		self.synopsis	= e.getElementsByTagName("synopsis")[0].childNodes[0].nodeValue.replace('<br/>', '')
		self.cover		= e.getElementsByTagName("poster")[0].attributes["href"].value
		casting			= e.getElementsByTagName("casting")[0].getElementsByTagName("castMember")
		self.directors	= self.get_cast_by_activity(casting, REA_CODE)
		self.actors		= self.get_cast_by_activity(casting, ACT_CODE)
		
	def get_cast_by_activity(self, casting, activity_code):
		people = list()
		for e in casting:
		    if int(e.getElementsByTagName("activity")[0].attributes["code"].value) == activity_code:
				people.append(e.getElementsByTagName("person")[0].childNodes[0].nodeValue)
		return people
		
	def parse_imdb(self, imdbfile_content):
		f = json.loads(imdbfile_content)
		self.rating = float(f['rating'])
		self.genres = f['genres'].split(',')
		#last non-null field of the url separated by /, stripped from its leading "tt" and converted to int, is the imdb ID.
		self.id_imdb = int(f["imdburl"].rsplit("/", 2)[1].lstrip("tt")) 
		
	def insert(self):
		mov = Movie()
		mov.title = self.title
		mov.year = self.year + "-01-01"
		mov.country = self.country
		mov.synopsis = self.synopsis
		mov.cover = self.cover
		
		mov.id_imdb = self.id_imdb
		mov.rating_imdb = self.rating
		
		mov.save() #ecrit dans la BDD
		#on doit save pour avoir une primary key avant de pouvoir faire les many to many
		
		#many to many
		#realisateurs
		for a in self.directors:
			a_forename = a.split(' ', 1)[0]
			a_name = a.split(' ', 1)[1]
			
			#checker les artistes deja presents
			qset = Artist.objects.filter(name = a_name, forename = a_forename)
			if qset.count() > 0 :
				mov.directed_by.add(qset[0])
			else : #creer ceux qui manquent
				dr = Artist(name = a_name, forename = a_forename)
				dr.save()
				mov.directed_by.add(dr)
		
		#acteurs (un peu de copier coller bien laid)
		for a in self.actors:
			a_forename = a.split(' ', 1)[0]
			a_name = a.split(' ', 1)[1]
			
			#checker les artistes deja presents
			qset = Artist.objects.filter(name = a_name, forename = a_forename)
			if qset.count() > 0 :
				mov.played_by.add(qset[0])
			else : #creer ceux qui manquent
				act = Artist(name = a_name, forename = a_forename)
				act.save()
				mov.played_by.add(act)
				
		#et encore du copier coller
		for g in self.genres:
			#checker les genres deja presents
			qset = Genre.objects.filter(name = g)
			if qset.count() > 0 :
				mov.genre_is.add(qset[0])
			else : #creer ceux qui manquent
				genre = Genre(name = g)
				genre.save()
				mov.genre_is.add(genre)
		
		mov.save() #on resauvegarde pour ecrire les many_to_many
		
