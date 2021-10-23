from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.utils import timezone


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

    def split_biography(self):
        return self.biography.split("\n")

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()




class Project(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True, default="title")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    url = URLField(max_length=100)
    posted_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.description

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")



