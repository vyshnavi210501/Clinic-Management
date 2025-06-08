from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Track_Record
from .serializer import TrackRecordSerializer
from djangoproject import permissions
from rest_framework import exceptions
from datetime import date as current_Date

# Create your views here.
class TrackRecordViewset(ModelViewSet):
    queryset=Track_Record.objects.all()
    serializer_class=TrackRecordSerializer
    permission_classes=[permissions.IsClinicAdminOfClinic]

    def perform_create(self, serializer):
        clinic=serializer.validated_data["clinic"]
        therapist=serializer.validated_data["therapist"]
        patient=serializer.validated_data["patient"]
        date=serializer.validated_data["date"]
        if date>current_Date.today():
            raise exceptions.ValidationError("Trackrecord can be recorded after visiting.")
        if self.request.user.role!='SuperAdmin' and clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannot create as its not assigned to clinic")
        if clinic.id!=therapist.clinic_id:
            raise exceptions.ValidationError("Therapist doesnt belong to clinic")
        if clinic.id!=patient.clinic_id:
            raise exceptions.ValidationError("patient doesnt belong to clinic")

        serializer.save()