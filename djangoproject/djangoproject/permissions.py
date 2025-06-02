from rest_framework.permissions import BasePermission,SAFE_METHODS
from clinic.models import Clinic

class IsSuperAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role=='Superadmin'

class IsClinicAdminOfClinic(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ClinicAdmin',"SuperAdmin"]
    
    def has_object_permission(self, request, view, obj):
        if request.user.role=='SuperAdmin':
            return True
        if request.user.role=='ClinicAdmin':
            if isinstance(obj,Clinic):
                return obj in Clinic.objects.all()
            if hasattr(obj,'clinic'):
                return obj.clinic in request.user.clinics.all()
        return(False)

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role=="Staff"