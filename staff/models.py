from django.db import models
from django.contrib.auth.models import AbstractUser

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Staff(AbstractUser):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    class Meta:
        abstract = True

class Doctor(Staff):
    specialization = models.CharField(max_length=100, blank=True, null=True)
    is_specialist = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

