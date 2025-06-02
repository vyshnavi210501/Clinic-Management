from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Clinic_Management

router=DefaultRouter()
router.register('',Clinic_Management,basename='clinics')

urlpatterns = [
    path('',include(router.urls))
]
