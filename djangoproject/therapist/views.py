from django.shortcuts import render
from rest_framework import viewsets,exceptions
from .models import Therapist
from .serializers import TherapistSerializer
from djangoproject import permissions
from django.shortcuts import get_object_or_404


# Create your views here.
class TherapistManagement(viewsets.ModelViewSet):
    queryset=Therapist.objects.all()
    serializer_class=TherapistSerializer
    permission_classes=[permissions.IsClinicAdminOfClinic]
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            if user.role=='SuperAdmin':
                return Therapist.objects.all()
            elif user.role=='ClinicAdmin':
                if self.action == 'list':
                # For list, restrict to therapists in user's clinics
                    clinic_ids = user.clinics.values_list('id', flat=True)
                    return Therapist.objects.filter(clinic__in=clinic_ids)
                else:
                    # For detail actions, return all to allow get_object() to find
                    return Therapist.objects.all()
        return Therapist.objects.none()

    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic']
        if self.request.user.role=="ClinicAdmin" and clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannot add therapist to the unassigned clinic")
        serializer.save()

    def get_object(self):
        obj = super().get_object()  # DRF handles fetching by pk automatically
        if self.request.user.role == 'ClinicAdmin' and obj.clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("You don't have permission to access this therapist.")
        return obj
