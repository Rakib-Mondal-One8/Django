from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20,null=True)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(null=True)
    fathers_name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"Roll No: {self.roll} - {self.name}"
    

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __self__(self):
        return f"Name: {self.name},Age: {self.age}"