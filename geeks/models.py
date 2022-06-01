from django.db import models
from datetime import datetime


# Create your models here.
# import the standard Django Model
# from built-in library

class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.CharField(max_length=120)
	manager = models.CharField(max_length=60)
	description = models.TextField(blank=True)
# declare a new model with a name "GeeksModel"


class GeeksModel(models.Model):
	# fields of the model
	title = models.CharField(max_length = 200)
	biography = models.TextField()

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.title


