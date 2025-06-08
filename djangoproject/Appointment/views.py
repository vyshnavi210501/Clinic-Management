from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Appointment
from .serializer import AppointmentSerializer
from djangoproject import permissions
from rest_framework.exceptions import PermissionDenied,ValidationError
# Create your views here.
class AppointmentViewset(ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
    permission_classes=[permissions.IsClinicAdminOrStaffOfClinic]

    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic']
        therapist=serializer.validated_data['therapist']
        patient=serializer.validated_data['patient']
        date=serializer.validated_data['date']
        start_time=serializer.validated_data['start_time']
        end_time=serializer.validated_data['end_time']
        if therapist.clinic_id!=clinic.id:
            raise ValidationError('Therapist doesnt belong to the selected clinic')
        if patient.clinic!=clinic:
            raise ValidationError('Patient doesnt belong to selected clinic')
        if self.request.user.role=='SuperAdmin':
            serializer.save()
            return
        overlapping_appointments = Appointment.objects.filter(
            therapist=therapist,
            date=date,
            status=Appointment.Status.BOOKED,
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if overlapping_appointments.exists():
            raise ValidationError('Therapist is already booked during this time slot.')
        if clinic not in self.request.user.clinics.all():
            raise PermissionDenied('Cannot add appointment who is not unauthorized for this clinic')
        
        serializer.save()




    