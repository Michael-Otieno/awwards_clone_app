from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField



# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField()
    url = URLField(max_length=100)
    