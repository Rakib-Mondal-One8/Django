from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to="accounts/uploads",blank=True,null=True)
