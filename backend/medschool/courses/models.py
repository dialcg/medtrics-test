from django.db import models


class Course(models.Model):
    """
    Represents a course.

    Attributes:
        name: The name of the course.
    """
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
