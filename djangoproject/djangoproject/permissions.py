from rest_framework.permissions import BasePermission,SAFE_METHODS
from clinic.models import Clinic
from rest_framework.exceptions import PermissionDenied

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
                return obj in request.user.clinics.all()
            if hasattr(obj,'clinic'):
                return obj.clinic in request.user.clinics.all()
        return(False)

class IsClinicAdminOrStaffOfClinic(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in ['ClinicAdmin',"SuperAdmin",'Staff']:
            return True
        raise PermissionDenied("User is not authenticated or User is not having required permission.")  
    def has_object_permission(self, request, view, obj):
        if request.user.role=='SuperAdmin':
            return True 
        if request.user.role in ['ClinicAdmin','Staff']:
            if hasattr(obj,'clinic'):
                return obj.clinic in request.user.clinics.all()
        return False
