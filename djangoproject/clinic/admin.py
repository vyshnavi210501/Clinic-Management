from django.contrib import admin
from .models import Clinic,User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'get_clinics', 'is_staff', 'is_superuser')
    def get_clinics(self, obj):
        return ", ".join([clinic.name for clinic in obj.clinics.all()]) if obj.clinics.exists() else "None"
    get_clinics.short_description = 'Clinics'

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'clinics')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role', 'clinics')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Clinic)
