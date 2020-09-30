from django.db import models

# Create your models here.

class Product(models.Model):
	Product_id = models.AutoField(primary_key=True)
	Product_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	price = models.FloatField(default=0)
	desc = models.TextField()
	pub_date = models.DateField()
	image = models.ImageField(upload_to='hireus/images', default="")

	def __str__(self):
		return self.Product_name

class booked(models.Model):
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	mob = models.CharField(max_length=12)
	Product_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	details = models.TextField()
	date = models.DateField()


	def __str__(self):
		return self.name
	

