import xml.dom.minidom #for allocine
import json #for imdb
from models import Movie

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
	
	#fields from imdb
	id_imdb = 0
	rating = 0.0
	genres = list()
	
	#other fields
	#slug
	#cover
	
	def get_cast_by_activity(self, casting, activity_code):
		people = list()
		for e in casting:
		    if int(e.getElementsByTagName("activity")[0].attributes["code"].value) == activity_code:
				people.append(e.getElementsByTagName("person")[0].childNodes[0].nodeValue)
		return people
		
	def parse_allocine_xml(self, xmlfile):
		f = xml.dom.minidom.parse(xmlfile)
		e = f.getElementsByTagName("movie")[0] #the global element containing everyting
		self.title		= e.getElementsByTagName("title")[0].childNodes[0].nodeValue
		self.title_en	= e.getElementsByTagName("originalTitle")[0].childNodes[0].nodeValue
		self.year		= e.getElementsByTagName("productionYear")[0].childNodes[0].nodeValue
		countrylist		= e.getElementsByTagName("nationalityList")[0]
		self.country	= countrylist.getElementsByTagName("nationality")[0].childNodes[0].nodeValue
		self.synopsis	= e.getElementsByTagName("synopsis")[0].childNodes[0].nodeValue
		casting			= e.getElementsByTagName("casting")[0].getElementsByTagName("castMember")
		self.directors	= self.get_cast_by_activity(casting, REA_CODE)
		self.actors		= self.get_cast_by_activity(casting, ACT_CODE)
		
	def parse_imdb(self, imdbfile):
		fp = open(imdbfile, 'r')
		f = json.load(fp)
		self.rating = float(f['rating'])
		self.genres = f['genres'].split(',')
		self.id_imdb = int(f["imdburl"].rsplit("/", 2)[1].lstrip("tt")) #last non-null field of the url separated by /, stripped from its leading "tt" and converted to int, is the imdb ID.
		
	def insert(self):
		mov = Movie()
		mov.title = self.title
		mov.year = self.year + "-01-01"
		mov.country = self.country
		mov.synopsis = self.synopsis
		
		mov.id_imdb = self.id_imdb
		mov.rating_imdb = self.rating
		
		mov.save() #ecrit dans la BDD
		#on doit save pour avoir une primary key avant de pouvoir faire les many to many
		
		#many to many
		#realisateurs
		for a in self.directors:
			a_forename = s.split(' ', 1)[0]
			a_name = s.split(' ', 1)[1]
			
			#checker les artistes déjà présents
			qset = Artist.objects.filter(name = a_name, forename = a_forename)
			if(qset.count() > 0)
				mov.directed_by.add(qset[0])
			else #creer ceux qui manquent
				dr = Artist(name = a_name, forename = a_forename)
				dr.save()
				mov.directed_by.add(dr)
		
		#acteurs
		for a in self.actors:
			a_forename = s.split(' ', 1)[0]
			a_name = s.split(' ', 1)[1]
			
			#checker les artistes déjà présents
			qset = Artist.objects.filter(name = a_name, forename = a_forename)
			if(qset.count() > 0)
				mov.directed_by.add(qset[0])
			else #creer ceux qui manquent
				act = Artist(name = a_name, forename = a_forename)
				act.save()
				mov.played_by.add(act)
				
		mov.save() #on resauvegarde pour écrire les many_to_many
		
