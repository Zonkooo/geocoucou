from apps.movies.views import *
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'', index, name='index'),
)