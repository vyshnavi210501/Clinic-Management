from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Clinic
from .serializer import Clinic_serializer
from rest_framework.response import Response
from djangoproject.permissions import IsClinicAdminOfClinic

# Create your views here.
class Clinic_Management(ModelViewSet):
    queryset=Clinic.objects.all()
    serializer_class=Clinic_serializer
    permission_classes=[IsClinicAdminOfClinic]

    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({'message':'Deleted successfully'})