import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from courses.models import Course


@pytest.mark.django_db
def test_course_list():
    Course.objects.create(name='Course 1')
    Course.objects.create(name='Course 2')

    client = APIClient()
    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == 'Course 1'
    assert response.data[1]['name'] == 'Course 2'

