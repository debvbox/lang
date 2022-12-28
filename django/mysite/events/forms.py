from django import forms
from django.forms import ModelForm
from .models import Venue

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




        
        
