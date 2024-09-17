from django.db.models import QuerySet
from .repositories import CourseRepository


class CourseService:
    """Handles business logic to interact with Courses."""

    def __init__(self):
        self.repository = CourseRepository()

    def list_courses(self) -> QuerySet:
        """
        Fetch all courses.

        Returns:
            QuerySet: QuerySet containing all courses.
        """

        return self.repository.get_all_courses()


