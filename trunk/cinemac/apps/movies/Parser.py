import xml.dom.minidom #for allociné
import json #for imdb

REA_CODE = 8002
ACT_CODE = 8001

class MovieParser:
	#fields from allocine
	title
	year
	country
	synopsis
	actors
	directors
	
	#fields from imdb
	id_imdb
	genres
	rating
	
	#other fields
	slug
	cover
	
	def parse_allocine_xml(xmlfile):
		f = xml.dom.minidom.parse(xmlfile)
		e = f.getElementsByTagName("movie")[0] #the global element containing everyting
		title		= e.getElementsByTagName("title")[0].childNodes[0].nodeValue
		year		= e.getElementsByTagName("productionYear")[0].childNodes[0].nodeValue
		countrylist	= e.getElementsByTagName("nationalityList")
		country		= countrylist.getElementsByTagName("nationality")[0].childNodes[0].nodeValue
		synopsis	= e.getElementsByTagName("synopsis")[0].childNodes[0].nodeValue
		casting		= e.getElementsByTagName("casting")[0].getElementsByTagName("castMember")
		directors	= get_cast_by_activity(casting, REA_CODE)
		actors		= get_cast_by_activity(casting, ACT_CODE)
		
		
	def get_cast_by_activity(casting, activity_code):
		people = list()
		for e in casting:
		    if int(e.getElementsByTagName("activity")[0].attributes["code"].value) == activity_code:
				people.append(e.getElementsByTagName("person")[0].childNodes[0].nodeValue)
		return people
		
	def parse_imdb(imdbfile)
		fp = open(imdbfile, 'r')
		f = json.load(fp)
		rating = float(f['rating'])
		genres = f['genres'].split(',')
		id_imdb = int(f["imdburl"].rsplit("/", 2)[1].lstrip("tt")) #last non-null field of the url separated by /, stripped from its leading "tt" and converted to int, is the imdb ID.
		
