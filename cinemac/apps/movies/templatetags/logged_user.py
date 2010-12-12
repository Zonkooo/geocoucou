#-*- coding: utf-8 -*-
from django import template
from apps.movies.models import *

register = template.Library()

class CurrentUserNode(template.Node):
	def render(self, context):
		try :
			m = Member.objects.get(contrib_user = context['user'])
			return_string = "Vous &ecirc;tes connect&eacute; en tant que %s" % m.pseudo
		except :
			return_string = "Vous n'&ecirc;tes pas connect&eacute"
			
		return return_string

def current_user_name(parser, token):
	return CurrentUserNode()
	
register.tag(current_user_name)
