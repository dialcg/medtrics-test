from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CourseViewSet


router = DefaultRouter()
router.register(r'', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
]
