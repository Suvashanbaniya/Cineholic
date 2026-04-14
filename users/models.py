from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=False, null=True)
    bio = models.TextField(blank=True,null=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    
    
    def __str__(self):
        return f'{self.username} {"✅" if self.is_verifed else "❌"}'
    