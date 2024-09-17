from django.db.models import QuerySet
from .models import Course


class CourseRepository:
    """Handles DB access for interacting with Courses."""

    def get_all_courses(self) -> QuerySet:
        """
        Retrieve all courses.

        Returns:
            QuerySet: QuerySet containing all courses.
        """

        return Course.objects.all()
