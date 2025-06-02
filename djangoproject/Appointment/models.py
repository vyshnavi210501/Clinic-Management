from django.db import models
from clinic.models import Clinic
from therapist.models import Therapist
from patient.models import Patient

# Create your models here.
class Appointment(models.Model):
    class Status(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    status=models.CharField(choices=Status.choices,default=Status.BOOKED,max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['therapist', 'date', 'start_time', 'end_time'],
                name='unique_appointment_per_therapist_time'
            )
        ]

    def __str__(self):
        return f'{self.therapist} {self.clinic} {self.patient}'
    