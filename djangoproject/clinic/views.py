from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Clinic
from .serializer import Clinic_serializer
from rest_framework.response import Response
from djangoproject.permissions import IsClinicAdminOfClinic
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class Clinic_Management(ModelViewSet):
    queryset=Clinic.objects.all()
    serializer_class=Clinic_serializer
    permission_classes=[IsClinicAdminOfClinic]

    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role=='SuperAdmin':
                return Clinic.objects.all()
            elif user.role=='ClinicAdmin':
                ids=user.clinics.values_list('id',flat=True)
                return Clinic.objects.filter(id__in=ids)

        return Clinic.objects.none()

    def create(self, request, *args, **kwargs):
        #added this method inorder to resolve data discrepancy issues bcz logged in user is able to create clinics without this method but unable 
        #to get assigned to user so only super admins can create clinics and can assign that clinic to some user using admin page
        if request.user.role == 'ClinicAdmin':
            raise PermissionDenied("ClinicAdmins are not allowed to create clinics.")
        return super().create(request, *args, **kwargs)
