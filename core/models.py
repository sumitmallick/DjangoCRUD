from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	contactno = models.IntegerField()

	def __str__(self):
		return self.name	