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
		
class AccountAccessNode(template.Node): #attention, code très sale
	def render(self, context):
		try : 
			m = Member.objects.get(contrib_user = context['user'])
			#on a réussi à choper l'user donc il est loggué
			return """<li class="toggleSubMenu"><span>Mon compte</span> 
						<ul class="subMenu"> 
							<li><a href="/profil/" title="Voir mon profil">Voir mon profil</a></li> 
							<li><a href="/login/?edit=1" title="Modifier mon profil">Modifier mon profil</a></li> 				 
							<li><a href="/listeMesInvit/" title="Mes invitations">Mes invitations</a></li> 				 
						</ul> 
					</li>"""
		except:
			return ""

def current_user_name(parser, token):
	return CurrentUserNode()	
register.tag(current_user_name)

def my_account_link(parser, token):
	return AccountAccessNode()
register.tag(my_account_link)

