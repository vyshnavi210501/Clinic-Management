from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Track_Record
from .serializer import TrackRecordSerializer
from djangoproject import permissions
from rest_framework import exceptions

# Create your views here.
class TrackRecordViewset(ModelViewSet):
    queryset=Track_Record.objects.all()
    serializer_class=TrackRecordSerializer
    permission_classes=[permissions.IsClinicAdminOfClinic]

    def perform_create(self, serializer):
        clinic=serializer.validated_data["clinic"]
        if clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannot create as its not assigned to clinic")
        serializer.save()