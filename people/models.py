from django.db import models
from event.models import Event
class People(models.Model):
	name = models.CharField(max_length=30)
	student_id = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	event = models.ManyToManyField(Event)
	def __unicode__(self):
		return self.name
