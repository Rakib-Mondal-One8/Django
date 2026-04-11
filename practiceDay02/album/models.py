from django.db import models
from django.utils.regex_helper import Choice

from musician.models import Musician


# Album Name
# One-to-Many Relationships with musician model
# Album release date
# Rating between 1-5

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name