import xml.dom.minidom

class MovieParser:
	id_imdb
	slug
	title
	cover
	year
	country
	synopsis	
	genres
	actors
	directors

	def parse_xml(param):
		f = xml.dom.minidom.parse(param)
		e = f.getElementsByTagName("movie")[0] #element global qui englobe tout
		title		= e.getElementsByTagName("title")[0].childNodes[0].nodeValue
		year		= e.getElementsByTagName("productionYear")[0].childNodes[0].nodeValue
		countrylist	= e.getElementsByTagName("nationalityList")
		country		= countrylist.getElementsByTagName("nationality")[0].childNodes[0].nodeValue
		synopsis	= e.getElementsByTagName("synopsis")[0].childNodes[0].nodeValue
		casting		= e.getElementsByTagName("casting")[0].getElementsByTagName("castMember")
		
		print e
		
	def get_cast_by_activity(casting, activity_code):
		people = list()
		for e in casting:
		    if str(e.attributes["activity"].value) == activity_code:
				people.append(e.getElementsByTagName("person")[0].nodeValue)
		return people
		
