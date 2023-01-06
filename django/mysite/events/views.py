from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event,Venue
from .forms import VenueForm,EventForm
from django.http import HttpResponse
import csv
#import from pdf file generator
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Import for pagination

from django.core.paginator import Paginator
#Generate CSV File Venue List

#Generate pdf FIle
# For pdf file install pip install reportlab

def venue_pdf(request):
    #Create Bytestream buffer
    buf = io.BytesIO()
    #Create Canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create text obj
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
   # lines = [
   #         "THis line"
    #        ]

    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename='venue.pdf')

def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename.venues.csv'

    #Create a csv writer
    writer = csv.writer(response)
    
    #Designate the Model
    venues = Venue.objects.all()

    #Create Header column
    writer.writerow(['Venue Name','Address','Zip code','Phone','Web Address','Email'])

    #Loop Th and output

    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.phone,venue.web,venue.email_address])

    return response


def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename.venues.txt'
    #Designate the Model
    venues = Venue.objects.all()
    
    #Create blank List
    lines = []
    #Loop Th and output

    for venue in venues:
        lines.append(f'Venue Name: {venue.name}\nAddress: {venue.address}\nZip code: {venue.zip_code}\nPhone: {venue.phone}\nWeb: {venue.web}\nEmail: {venue.email_address}\n\n')


   # lines = ["This is line 1\n"
   #         "This line 2\n",
   #         "This line 3\n",

   #         ]
    response.writelines(lines)
    return response

def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venue')


def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')
    

def update_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    #instance is for data that with wanna fill out the form
    form = EventForm(request.POST or None,instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    
    return render(request,'events/update_event.html',{
		'event':event,
		'form':form,
		})

def add_event(request):
	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_event?submitted=True')
	else:
		form = EventForm
		# USER SUBMITTER THE FORM
		if 'submitted' in request.GET:
			submitted = True

	
	return render(request,'events/add_event.html',
		{'form':form,'submitted':submitted})

def update_venue(request,venue_id):
	venue = Venue.objects.get(pk=venue_id)

	#instance is for data that with wanna fill out the form
	form = VenueForm(request.POST or None,instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venue')

	return render(request,'events/update_venue.html',{
		'venue':venue,
		'form':form,
		})

def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)

		return render(request,'events/search_venues.html',{
			'searched':searched,
			'venues':venues,
			})
	else:
		return render(request,'events/search_venues.html',{})

def show_venue(request,venue_id):
	venue = Venue.objects.get(pk=venue_id)



	return render(request,'events/show_venue.html',{
		'venue':venue,
		})

def list_venue(request):
    #venue_list = Venue.objects.all()
    #Set up Pagination
    venues_per_page = 2
    p = Paginator(Venue.objects.all(),venues_per_page)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a"*venues.paginator.num_pages
    return render(request,'events/venue.html',
            {'venues':venues,'nums':nums})

def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	else:
		form = VenueForm
		# USER SUBMITTER THE FORM
		if 'submitted' in request.GET:
			submitted = True

	
	return render(request,'events/add_venue.html',
		{'form':form,'submitted':submitted})


def all_events(request):
	event_list = Event.objects.all().order_by('-name')
	return render(request,'events/event_list.html',
		{'event_list':event_list})

#passing path converters (year,month)
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):

	name = "meme"
	month = month.capitalize()

	#Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	#create calendar
	cal = HTMLCalendar().formatmonth(year,month_number)

	#get Current year
	now = datetime.now()
	current_year = now.year

	#get current time
	time = now.strftime('%I:%M %p')

	return render(request,'events/home.html',
		{
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"name":name,
		"current_year":current_year,
		"time":time,
		})
