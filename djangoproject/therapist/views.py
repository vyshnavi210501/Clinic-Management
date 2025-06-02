from django.shortcuts import render
from rest_framework import viewsets,exceptions
from .models import Therapist
from .serializers import TherapistSerializer
from djangoproject import permissions
from silk.profiling.profiler import silk_profile
from django.utils.decorators import method_decorator
from django.views.decorators import cache


# Create your views here.
class TherapistManagement(viewsets.ModelViewSet):
    queryset=Therapist.objects.all()
    serializer_class=TherapistSerializer
    permission_classes=[permissions.IsClinicAdminOfClinic]

    @silk_profile(name='therapist-silk')
    @method_decorator(cache.cache_page(60*15))
    def list(self,request,*args,**kwargs):
        return super().list(request,*args,**kwargs)


    def perform_create(self, serializer):
        clinic=serializer.validated_data['clinic_id']
        if self.request.user.role=="ClinicAdmin" and clinic not in self.request.user.clinics.all():
            raise exceptions.PermissionDenied("Cannot add therapist to the unassigned clinic")
        serializer.save()
        cache.clear()

    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)
    