
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Athlete(models.Model):
    
    username = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='ksp.jpg', upload_to='profile_images')
    date = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return (f'{self.member.username}') 






# Create your models here.
