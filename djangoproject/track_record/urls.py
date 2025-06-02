from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TrackRecordViewset

router=DefaultRouter()
router.register('',TrackRecordViewset)

urlpatterns = [
    path('',include(router.urls))
]