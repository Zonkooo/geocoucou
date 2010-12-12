from django import template
from apps.movies.models import *

register = template.Library()

class CurrentUserNode(template.Node):
	def render(self, context):
		#m = Member.objects.get(contrib_user = context['user'])
		return context#['user'] #m.pseudo

def current_user_name(parser, token):
	return CurrentUserNode()
	
register.tag(current_user_name)
