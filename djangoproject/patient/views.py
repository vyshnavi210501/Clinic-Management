from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework import viewsets,exceptions
from djangoproject.permissions import IsClinicAdminOrStaffOfClinic

# Create your views here.
class PatientManagement(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    permission_classes=[IsClinicAdminOrStaffOfClinic]

    def get_queryset(self):
        user=self.request.user
        if user.role=='SuperAdmin':
            return Patient.objects.all()
        elif user.role in ['ClinicAdmin','Staff']:
            if self.action=='list':
                ids=user.clinics.values_list('id',flat=True)
                return Patient.objects.filter(clinic__in=ids)
            else:
                return Patient.objects.all()
        else:
            raise exceptions.PermissionDenied("No matching patients found")


    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic']
        if self.request.user.role in['ClinicAdmin','Superadmin','Staff'] and clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannot add patient for specified clinic due to persmission issue")
        serializer.save()