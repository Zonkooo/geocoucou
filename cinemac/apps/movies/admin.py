from django.contrib import admin
from apps.movies.models import *

#class AuthorAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Course)
admin.site.register(CourseComment)
admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(CommentMovie)
admin.site.register(CommentEvent)
admin.site.register(Event)
admin.site.register(Member)