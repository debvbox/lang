from django import forms
from django.forms import ModelForm
from .models import Venue,Event

#Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name','address','zip_code','phone','web','email_address',)

		#can change inport type on form or set the according type
        #and add some style

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name '}),
			'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
			'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
		}
		#can use for change the label below textbox
		labels = {
            'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',
        }

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name','event_date','venue','manager','attendees','description',)

		#can change inport type on form or set the according type
        #and add some style

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name '}),
			'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}),
			'venue': forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
			'manager': forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
		}
		#can use for change the label below textbox
		labels = {
            'name': '',
			'event_date': '',
			'venue': 'Venue',
			'manager': 'Manager',
			'attendees': 'Attendees',
			'description': '',
        }




        
        
