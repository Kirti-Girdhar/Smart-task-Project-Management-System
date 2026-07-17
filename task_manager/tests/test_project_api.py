from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from users.models import CustomUser
from projects.models import Project


class ProjectAPITest(APITestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            username="user1",
            password="testpass123"
        )

        self.user2 = CustomUser.objects.create_user(
            username="user2",
            password="testpass123"
        )

        self.client = APIClient()

    def test_create_project(self):
        self.client.force_authenticate(user=self.user1)

        data = {
            "name": "Task Manager",
            "members": [self.user1.id]
        }

        response = self.client.post("/api/projects/", data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().name, "Task Manager")
        self.assertEqual(Project.objects.first().owner, self.user1)

    def test_user_can_only_see_own_projects(self):
        Project.objects.create(
            name="User1 Project",
            owner=self.user1
        )
        Project.objects.create(
            name="User2 Project",
            owner=self.user2
        )

        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/projects/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "User1 Project")

    def test_unauthenticated_user_cannot_access_projects(self):
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, 401)
