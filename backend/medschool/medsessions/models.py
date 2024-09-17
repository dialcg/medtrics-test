from django.db import models
from courses.models import Course


class Location(models.Model):
    """
    Represents a location where sessions are held.

    Attributes:
        name: The name of the location.
    """
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sessions")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.course.name} - {self.name}'


class SessionSchedule(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="schedules")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['session', 'date', 'start_time', 'location']

    def __str__(self):
        return f'{self.session.name} on {self.date} at {self.location}'

