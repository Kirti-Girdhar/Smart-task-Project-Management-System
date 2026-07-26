from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Organization


User = get_user_model()


class OrganizationTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="kirti",
            password="test123"
        )

        self.client.force_authenticate(
            self.user
        )

    def test_create_organization(self):
        data = {
            "name": "ABC Software",
            "description": "Testing organization"
        }
        response = self.client.post(
            "/api/organizations/",
            data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Organization.objects.count(),
            1
        )

        self.assertEqual(
            Organization.objects.first().owner,
            self.user
        )