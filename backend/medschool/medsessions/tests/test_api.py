import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from courses.models import Course
from medsessions.models import SessionSchedule, Location, Session


@pytest.mark.django_db
def test_session_schedule_list():
    course = Course.objects.create(name='Course1')
    location1 = Location.objects.create(name='Location1')
    location2 = Location.objects.create(name='Location2')

    session1 = Session.objects.create(name='Session1', course=course, description='Description1')
    session2 = Session.objects.create(name='Session2', course=course, description='Description2')

    SessionSchedule.objects.create(
        session=session1,
        date='2024-09-15',
        start_time='10:00:00',
        end_time='12:00:00',
        location=location1
    )
    SessionSchedule.objects.create(
        session=session2,
        date='2024-09-16',
        start_time='14:00:00',
        end_time='16:00:00',
        location=location2
    )

    client = APIClient()
    url = reverse('sessions-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['session']['id'] == session1.id
    assert response.data[1]['session']['id'] == session2.id


@pytest.mark.django_db
def test_location_list():
    Location.objects.create(name='Location1')
    Location.objects.create(name='Location2')

    client = APIClient()
    url = reverse('locations-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == 'Location1'
    assert response.data[1]['name'] == 'Location2'
