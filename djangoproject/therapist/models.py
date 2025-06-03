from django.db import models
from clinic.models import Clinic
from datetime import time
from django.core.exceptions import ValidationError

# Create your models here.
class Therapist(models.Model):
    name=models.CharField(max_length=50,null=False)
    specialization=models.CharField(max_length=20,null=False)
    experience_years=models.FloatField(null=False)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    contact_number=models.CharField(max_length=20,null=False,unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def check_date(self):
        if self.end_time<self.start_time:
            raise ValidationError("End time must be greater than start time")

    def __str__(self):
        return self.name
