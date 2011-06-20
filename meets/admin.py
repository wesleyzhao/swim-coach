from meets.models import Meet,Event,Lane,Person,PhoneNumber
from django.contrib import admin

class LaneInline(admin.TabularInline):
	model = Lane
	extra = 6

class EventInline(admin.TabularInline):
	model = Event
	extra = 3
	
	
class MeetAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields':['name']}),
		('Day of event',{'fields':['date']}),
		('Slug', 		{'fields':['slug']}),
	]
	inlines = [EventInline]
	prepopulated_fields = {"slug": ("name",)}
	
class PersonAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','event_number','lane_number')
	
class EventAdmin(admin.ModelAdmin):
	inlines = [LaneInline]
	
admin.site.register(Meet,MeetAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Lane)
admin.site.register(Person,PersonAdmin)
admin.site.register(PhoneNumber)