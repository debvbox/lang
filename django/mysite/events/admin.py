from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event



admin.site.register(MyClubUser)
#admin.site.register(Event)

#personalize admin area visualization
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name','address','zip_code')
	ordering = ('name',)
	search_fields = ('name','address')


#check Events in admin area to see the features added below
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name','venue'),'event_date','description','manager',)
	list_display = ('name','event_date',)
	list_filter = ('event_date','venue')
	ordering = ('-event_date',)