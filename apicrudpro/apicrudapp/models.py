from django.db import models


class Student(models.Model):
	sid=models.IntegerField(primary_key=True)
	sname =models.CharField(max_length=20)
	saddress=models.CharField(max_length=30)
	def __str__(self):
		return(self.sname)
