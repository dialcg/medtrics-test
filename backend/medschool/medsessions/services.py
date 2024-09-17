from typing import Optional
from django.db.models import QuerySet
from .repositories import SessionScheduleRepository, LocationRepository


class LocationService:
    """Handles business logic to interact with Locations."""

    def __init__(self):
        self.repository = LocationRepository()

    def list_locations(self) -> QuerySet:
        """
        Fetch all locations.

        Returns:
            QuerySet: QuerySet containing all locations.
        """
        return self.repository.get_all_locations()


class SessionScheduleService:
    """Handles business logic to interact with schedules (Sessions)."""

    def __init__(self):
        self.repository = SessionScheduleRepository()

    def list_schedules(
        self,
        course_id: Optional[str] = None,
        date: Optional[str] = None,
        location_id: Optional[str] = None
    ) -> QuerySet:
        """
        Fetch session schedules filtered by course, date, and location.

        Args:
            course_id (Optional[str]): Course ID for filtering schedules.
            date (Optional[str]): Date for filtering schedules.
            location_id (Optional[str]): Location ID for filtering schedules.

        Returns:
            QuerySet: Filtered session schedules queryset.
        """
        return self.repository.filter_schedules(course_id=course_id, date=date, location_id=location_id)
