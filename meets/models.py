from django.db import models
import datetime

# Create your models here.
class Meet(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('date of meet')
	slug = models.SlugField(max_length=200)
	def __unicode__(self):
		return self.name
	def has_meet_passed(self):
		return self.date()<datetime.date.today()
	has_meet_passed.short_description = 'Has the meet happened?'
	
class Person(models.Model):
	lane_number = models.IntegerField(max_length=11,null=True,blank=True)
	event_number = models.IntegerField(max_length=11,null=True,blank=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	is_coach = models.BooleanField()
	def __unicode__(self):
		return self.first_name+" "+self.last_name
	
class Event(models.Model):
	meet = models.ForeignKey(Meet)
	name = models.CharField(max_length=200)
	number = models.IntegerField()
	def __unicode__(self):
		return self.name
		
	
class Lane(models.Model):
	LANE_CHOICES= (
		(1,'lane 1'),
		(2,'lane 2'),
		(3,'lane 3'),
		(4,'lane 4'),
		(5,'lane 5'),
		(6,'lane 6'),
		(7,'lane 7'),
		(8,'lane 8')
	)
	event = models.ForeignKey(Event)
	number = models.IntegerField(choices=LANE_CHOICES)
	person = models.ForeignKey(Person,null=True,blank=True,default=None)
	def __unicode__(self):
		return "lane "+ str(self.number)

	
class PhoneNumber(models.Model):
	person = models.ForeignKey(Person)
	owner_name = models.CharField(max_length=200)
	number = models.BigIntegerField(max_length=11)
	def __unicode__(self):
		return str(self.number)
