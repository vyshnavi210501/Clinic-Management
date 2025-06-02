from django.db import models
from clinic.models import Clinic
from therapist.models import Therapist
from patient.models import Patient

# Create your models here.
class Track_Record(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    date=models.DateField()
    treatment_notes=models.TextField(max_length=1000)
    next_followup_date=models.DateField(null=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['patient','therapist','date'],
                name='unique_constraint_patient_date_therapist'
            )
        ]

    def __str__(self):
        return f'{self.patient}-{self.date}'