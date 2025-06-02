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
    permission_classes=[permissions.IsClinicAdminOfClinic]

    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic']
        therapist=serializer.validated_data['therapist']
        patient=serializer.validated_data['patient']
        if therapist.clinic_id!=clinic:
            raise ValidationError('Therapist doesnt belong to the selected clinic')
        if patient.clinic!=clinic:
            raise ValidationError('Patient doesnt belong to selected clinic')
        if self.request.user.role=='SuperAdmin':
            serializer.save()
            return
        if clinic not in self.request.user.clinics.all():
            raise PermissionDenied('Cannot add appointment who is not unauthorized for this clinic')
        
        serializer.save()




    