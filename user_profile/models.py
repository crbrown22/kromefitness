from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    members = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='ksp.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.members.last_name} {self.members.first_name} / {self.members.username}'

# Create your models here.
