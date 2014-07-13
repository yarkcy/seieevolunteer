from django import template
from event.models import Event
register = template.Library()

def show_event_name(format_string):
	try:
		p = Event.objects.get(name=format_string)
		return p.id
	except UnicodeEncodeError:
		return ''
register.simple_tag(show_event_name)