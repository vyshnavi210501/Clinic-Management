from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Clinic(models.Model):
    name=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=20,null=False)
    state=models.CharField(max_length=30,null=False)
    contact_number=models.CharField(max_length=15,null=False,unique=True)
    email=models.EmailField(max_length=50,null=False)
    opening_time=models.TimeField(max_length=20,default='09:00:00')
    closing_time=models.TimeField(max_length=20,default='18:00:00')

    def __str__(self):
        return(self.name)

class User(AbstractUser):
    ROLE_CHOICES=[
        ('SuperAdmin','SuperAdmin'),
        ('ClinicAdmin','ClinicAdmin'),
        ('Staff','Staff')
    ]

    role=models.CharField(choices=ROLE_CHOICES,max_length=15)
    clinics=models.ManyToManyField(Clinic,blank=True,related_name='users')

    def __str__(self):
        return f"{self.username} ({self.role})"

