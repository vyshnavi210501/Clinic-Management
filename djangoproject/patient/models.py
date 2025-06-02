from django.db import models
from clinic.models import Clinic

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=50,null=False)
    dob=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=30,null=False)
    contact_number=models.CharField(max_length=20,null=False,unique=True)
    address=models.CharField(max_length=200,null=False)
    medical_history=models.CharField(max_length=500,null=False)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)