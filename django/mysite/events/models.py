from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
	name = models.CharField('Venue Name',max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip code',max_length=55)
	phone = models.CharField('Contact Phone',max_length=8,blank=True)
	web = models.URLField('Website Addres',blank=True)
	email_address = models.EmailField('Email',blank=True)

	def __str__(self):
		return self.name

class MyClubUser(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField('User Email')


	def __str__(self):
		return self.first_name + ' ' + self.last_name



class Event(models.Model):
	name = models.CharField('Event name',max_length=120,)
	event_date = models.DateTimeField('Event date')
	venue = models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120) 
	#manager = models.CharField(max_length=120)
	#if a manager leave then put null value instead
	manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser,blank=True)

#allow add model to admin panel
	def __str__(self):
		return self.name

     
