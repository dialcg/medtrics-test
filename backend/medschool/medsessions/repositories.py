from django.db.models import QuerySet
from .models import SessionSchedule, Location


class LocationRepository:
    """Handles DB access for interacting with Locations."""

    def get_all_locations(self) -> QuerySet:
        """
        Retrieve all locations.

        Returns:
            QuerySet: QuerySet containing all locations.
        """

        return Location.objects.all()


class SessionScheduleRepository:
    """Handles DB access for interacting with schedules (Sessions)."""

    def filter_schedules(
        self,
        course_id: str = None,
        date: str = None,
        location_id: str = None
    ) -> QuerySet:
        """
        Filter session schedules by course, location, and date.

        Args:
            course_id (str, optional): Course ID to filter by.
            date (str, optional): Date to filter by.
            location_id (str, optional): Location ID to filter by.

        Returns:
            QuerySet: Filtered session schedules.
        """
        schedules = SessionSchedule.objects.select_related('session', 'session__course', 'location').all()

        if course_id:
            schedules = schedules.filter(session__course_id=course_id)
        if date:
            schedules = schedules.filter(date=date)
        if location_id:
            schedules = schedules.filter(location_id=location_id)

        return schedules
