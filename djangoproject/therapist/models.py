from django.db import models
from clinic.models import Clinic

# Create your models here.
class Therapist(models.Model):
    name=models.CharField(max_length=50,null=False)
    specialization=models.CharField(max_length=20,null=False)
    experience_years=models.FloatField(null=False)
    clinic_id=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    availability_schedule=models.CharField(max_length=50,null=False)
    contact_number=models.CharField(max_length=20,null=False,unique=True)

    def __str__(self):
        return self.name
