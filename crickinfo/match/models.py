from django.db import models

# Create your models here.
# create table customer(id int primarykey, name varchar(250))
class Customer(models.Model):
	name= models.CharField(max_length=250)

	def __str__(self):
		return self.name


