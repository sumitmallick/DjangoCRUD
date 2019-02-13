from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=30)
	category = models.CharField(max_length=30)
	price = models.IntegerField(default='19')
	date_created = models.DateTimeField()
	stock = models.BooleanField()
	def __str__(self):
		return self.name

	