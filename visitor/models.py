from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Add more roles when there need to create an role who can also login and have a profile
    ROLES = [
        ('VS', 'Visitor'),
        ('DC', 'Doctor'),
        ('RC', 'Receptionist'),
        ('LB', 'Lab_technician')
    ]
    role = models.CharField(max_length=2, choices=ROLES)
    profile_id = models.BigIntegerField()

class Visitor_profile(models.Model):
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)