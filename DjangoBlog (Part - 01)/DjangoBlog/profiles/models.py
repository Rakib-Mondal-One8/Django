from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(Author,on_delete=models.CASCADE,max_length=100)
    about = models.TextField()