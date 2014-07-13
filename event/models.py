from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=100)
	discription = models.TextField(max_length=400)
	isActive = True
	id = models.AutoField(primary_key=True)

class DateTime(models.Model):
	name = models.CharField(max_length=100)
	event = models.ForeignKey(Event)

	def __unicode__(self):
		return self.name
