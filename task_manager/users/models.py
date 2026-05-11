from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),)
    phone_number = models.CharField(max_length=15,blank=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='employee')
    profile_image = models.ImageField(upload_to='profiles/',null=True,blank=True)

    def __str__(self):
        return self.username