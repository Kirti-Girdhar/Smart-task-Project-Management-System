from django.db import models
from django.conf import settings

class Organization(models.Model):
    name= models.CharField(max_length=100, unique=True)
    owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_organizations')
    description= models.TextField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering= ["name"]

    def __str__(self):
        return self.name