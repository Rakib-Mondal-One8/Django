from django.db import models

from category.models import Category

"""
taskTitle 
taskDescription 
is_completed by default False
Task Assign Date
"""

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	is_completed = models.BooleanField(default=False)
	assigned_date = models.DateField()
	category = models.ManyToManyField(Category)

	def __str__(self):
		return f"{self.title} - {self.assigned_date}"