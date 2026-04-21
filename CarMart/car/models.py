from django.db import models
from brand.models import Brand
from django.contrib.auth.forms import User

# Create your models here.
class Car(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand')
    image = models.ImageField(upload_to='car/uploads/',blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.name}"

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
