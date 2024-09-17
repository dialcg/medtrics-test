from rest_framework import viewsets
from .services import CourseService
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles API for interacting with Courses."""

    serializer_class = CourseSerializer

    def get_queryset(self):
        service = CourseService()
        return service.list_courses()
