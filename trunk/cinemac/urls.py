# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import *
import settings

admin.autodiscover()
# waouh !


urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$',
	'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
		'show_indexes': True,
		},
	),
)

urlpatterns += patterns('',
    # Example:
     (r'', include('apps.movies.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
