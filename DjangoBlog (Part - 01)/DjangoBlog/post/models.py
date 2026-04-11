from django.db import models
from author.models import Author
from category.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.CharField(default='https://cdn.britannica.com/92/152292-050-EAF28A45/Bald-eagle.jpg')
    category = models.ManyToManyField(Category)
    content = models.TextField()
