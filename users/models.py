from django.contrib.auth.models import AbstractUser, User,Group,GroupManager
from django.db import models



class CustomUser(AbstractUser):
    pass




# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, blank=True, default='Null')
    phone_no = models.CharField(max_length=100, blank=True, default='Null')
    profile_image = models.ImageField(upload_to='static/user/images', blank=True, null=True)

    def __str__(self):
        return self.user.username
