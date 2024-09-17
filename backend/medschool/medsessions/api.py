from rest_framework import viewsets
from .services import SessionScheduleService, LocationService
from .serializers import SessionScheduleSerializer, LocationSerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles API for interacting with Locations."""

    serializer_class = LocationSerializer

    def get_queryset(self):
        service = LocationService()
        return service.list_locations()


class SessionScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles API for interacting with Schedules (Sessions)."""

    serializer_class = SessionScheduleSerializer

    def get_queryset(self):
        service = SessionScheduleService()

        course_id = self.request.query_params.get('course')
        date = self.request.query_params.get('date')
        location_id = self.request.query_params.get('location')

        return service.list_schedules(course_id=course_id, date=date, location_id=location_id)
