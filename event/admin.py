from django.contrib import admin

from event.models import Event
from event.models import DateTime

class DateInline(admin.TabularInline):
	model = DateTime

class EventAdmin(admin.ModelAdmin):
	inlines  = [DateInline,]

class DateTimeAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(Event, EventAdmin)
admin.site.register(DateTime,DateTimeAdmin)

