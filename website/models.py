from django.db import models

# Create your models here.

class Franchise(models.Model):
	firstName= models.CharField(max_length=10)
	email_address= models.CharField(max_length=100)
	phone_no= models.CharField(max_length=15)
	occupation= models.CharField(max_length=1000)
	City_name= models.CharField(max_length=100)
	pincodes= models.CharField(max_length=100)
	investment= models.CharField(max_length=100)