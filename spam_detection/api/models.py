from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   phone_number = models.CharField(max_length=15, unique=True)
   email = models.EmailField(blank=True, null=True)
   
   groups = models.ManyToManyField( 
      'auth.Group', 
      related_name='api_users', 
      blank=True,
      help_text='The groups this user belongs to.', 
      verbose_name='groups', 
)
   user_permissions = models.ManyToManyField(
      'auth.Permission',
      related_name='api_user',
      blank=True,
      help_text='Specific permissions for this user.',   
      verbose_name ='user permissions',
   )
   
class Contact(models.Model):
   owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   phone_number = models.CharField(max_length=15)
   email = models.EmailField(blank=True, null=True)

class SpamReport(models.Model):
   phone_number = models.CharField(max_length=15)
   reported_by = models.ForeignKey(User, on_delete=models.CASCADE)