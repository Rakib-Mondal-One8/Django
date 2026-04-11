from django.db import models

# First Name
# Last Name
# Email
# Phone number
# Instrument Type

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField()
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name