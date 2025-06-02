from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TherapistManagement

router=DefaultRouter()
router.register('',TherapistManagement)

urlpatterns = [
    path('',include(router.urls))
]