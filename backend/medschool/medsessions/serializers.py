from rest_framework import serializers
from courses.serializers import CourseSerializer
from .models import SessionSchedule, Session, Location


class SessionSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Session
        fields = ['id', 'name', 'course']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'name',]


class SessionScheduleSerializer(serializers.ModelSerializer):

    session = SessionSerializer()
    location = LocationSerializer()

    class Meta:
        model = SessionSchedule
        fields = ['id', 'session', 'location', 'date', 'start_time', 'end_time']
