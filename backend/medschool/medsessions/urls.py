from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api import SessionScheduleViewSet, LocationViewSet


router = DefaultRouter()
router.register(r'session-schedules', SessionScheduleViewSet, basename='sessions')
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
]

