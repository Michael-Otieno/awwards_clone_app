from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to ='images/',null=True, blank=True)
    biography = models.TextField(blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def update_bio(self,biography):
        self.biography=biography
        self.save()
    
    def delete_profile(self):
        self.delete()



class Project(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True, default="title")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    url = URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")



