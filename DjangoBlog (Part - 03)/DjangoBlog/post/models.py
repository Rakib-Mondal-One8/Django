from django.db import models
from category.models import Category
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/uploads/", blank=True, null=True)
    category = models.ManyToManyField(Category)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_on}"
