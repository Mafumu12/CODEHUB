from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class UserProfile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to ='profile_images',default='user.png' )
    cover_photo = models.ImageField(upload_to ='profile_images',default='cover-photo.png' )
    profile_id = models.UUIDField(default=uuid.uuid4, editable = False, unique=True, primary_key=True)
    date_joined = models.DateTimeField(auto_now=True)
    about = models.TextField()

    def __str__(self):
        return self.username
     

   