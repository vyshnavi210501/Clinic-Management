from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework import viewsets,exceptions
from djangoproject import permissions

# Create your views here.
class PatientManagement(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    permission_classes=[permissions.IsClinicAdminOfClinic]

    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic']
        if self.request.user.role in['ClinicAdmin','Superadmin'] and clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannpt add patient for specified clinic due to persmission issue")
        serializer.save()