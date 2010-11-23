from django.db import models

class Genre(models.Model):
	slug 		= models.SlugField(max_length = 255)
	name 		= models.CharField(max_length = 255)
	
	def __unicode__(self):
		return "%u" % (self.name)
		
class Artist(models.Model):
	slug 		= models.SlugField(max_length = 255)
	name 		= models.CharField(max_length = 255)
	forename	= models.CharField(max_length = 255)
	
	def __unicode__(self):
		return "%u %u" % (self.forename, self.name)
		
class Course(models.Model):
	slug 		= models.SlugField(max_length = 255)
	year		= models.PositiveSmallIntegerField()
	topic		= models.CharField(max_length = 255)
	teacher		= models.CharField(max_length = 255)
	
	def __unicode__(self):
		return "%u" % (self.topic)
		
class CourseComment(models.Model):
	slug 		= models.SlugField(max_length = 255)
	date		= models.DateTimeField(auto_now_add=True)
	comment		= models.TextField()
	
	course		= models.ForeignKey('Course')
	movie		= models.ForeignKey('Movie')
	author		= models.ForeignKey('Member')
	
	def __unicode__(self):
		return "%u" % (self.comment)
		
class Movie(models.Model):
	id_imdb		= models.PositiveIntegerField()
	slug 		= models.SlugField(max_length = 255)
	title 		= models.CharField(max_length = 255)
	cover		= models.ImageField(upload_to='media/img/')
	year 		= models.DateField()
	country		= models.CharField(max_length = 255)
	synopsis	= models.TextField()
	
	genre_is	= models.ManyToManyField('Genre')
	played_by	= models.ManyToManyField('Artist')
	directed_by	= models.ManyToManyField('Artist')
	
	def __unicode__(self):
		return "%u (%u)" % (self.title, self.year.year)
		

class Rate(models.Model):
	slug 		= models.SlugField(max_length = 255)
	value		= models.PositiveSmallIntegerField()
	comment		= models.TextField()
	
	movie		= models.ForeignKey('Movie')
	author		= models.ForeignKey('Member')
	
	def __unicode__(self):
		return "%u" % (self.value)
		

class CommentMovie(models.Model):
	slug 		= models.SlugField(max_length = 255)
	date		= models.DateTimeField(auto_now_add=True)
	content		= models.TextField()
	
	movie		= models.ForeignKey('Movie')
	author		= models.ForeignKey('Member')
	
	def __unicode__(self):
		return "%u" % (self.comment)
		
class CommentEvent(models.Model):
	slug 		= models.SlugField(max_length = 255)
	date		= models.DateTimeField(auto_now_add=True)
	content		= models.TextField()
	
	movie		= models.ForeignKey('Event')
	author		= models.ForeignKey('Member')
	
	def __unicode__(self):
		return "%u" % (self.comment)
		
class Event(models.Model):
	slug 		= models.SlugField(max_length = 255)
	date		= models.DateTimeField()
	location	= models.CharField(max_length = 255)
	description	= models.TextField()
	
	movie		= models.ForeignKey('Movie')
	creator		= models.ForeignKey('Member')
	
	def __unicode__(self):
		return "%u, %u" % (self.location, self.date)
		
class Member(models.Model):
	slug 		= models.SlugField(max_length = 255)
	pseudo		= models.CharField(max_length = 255)
	mail		= models.EmailField();
	password	= models.CharField(max_length = 255);
	date_joined	= models.DateTimeField(auto_now_add=True)
	class_year	= models.DateField();
	avatar		= models.ImageField(upload_to='media/img/avatars/')
	
	def __unicode__(self):
		return "%u" % (self.pseudo)
		
