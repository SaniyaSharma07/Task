# from django.db import models
from pymodm import MongoModel ,fields
from datetime import datetime
# Create your models here.
class Provider(MongoModel): 
	providerId=fields.IntegerField()
	speciality=fields.CharField()
	firstName=fields.CharField()
	lastName=fields.CharField()
	gender=fields.CharField(choices=('F','M','O'))
	zipcode=fields.IntegerField()

	class Meta:
		collection_name='Provider'
		final=True

class Patient(MongoModel):
	patientId=fields.IntegerField()
	firstName=fields.CharField()
	lastNname=fields.CharField()
	height=fields.IntegerField()
	gender=fields.CharField(choices=('F','M','O'))

	class Meta:
		collection_name='Patient'
		final=True

class Referrals(MongoModel):
	# ref_id=fields.IntegerField()
	patientId=fields.IntegerField()	
	referredById=fields.IntegerField()
	referredToId=fields.IntegerField()
	createdOn=fields.DateTimeField(default=datetime.now())
	updatedOn=fields.DateTimeField(default=datetime.now())
	status=fields.CharField(choices=('ACCEPT','DECLINE','PENDING'),default="PENDING")
	remarks=fields.CharField()
	class Meta:
		collection_name='Referrals'
		final=True


class Appointments(MongoModel):
	# appointment_id=fields.IntegerField()
	providerId=fields.IntegerField()
	patientId=fields.IntegerField()
	date=fields.DateTimeField()
	status=fields.CharField(choices=('PENDING','SCHEDULED','ONGOING'),default="PENDING")
	class Meta:
		collection_name='Appointments'
		final=True
