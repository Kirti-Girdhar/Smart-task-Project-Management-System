from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.urls import reverse
from django.utils import timezone

from users.models import CustomUser
from tasks.models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user= CustomUser.objects.create_user(
            username = 'testuser',
            password = 'testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):

        data = {
        'title': 'Test Task',
        'description': 'Testing API',
        'status': 'pending',
        'priority': 'high',
        'due_date': timezone.now() 
    }
        response = self.client.post(reverse('task-list'),data)
        print(response.data)
        self.assertEqual(response.status_code,201)

        self.assertEqual(Task.objects.count(),1)

        self.assertEqual(Task.objects.first().title,'Test Task')
    
    def test_unauthenticated_user_cannot_create_task(self):
        self.client.force_authenticate(
        user=None
        )
        data = {'title': 'Unauthorized Task'}

        response = self.client.post(reverse('task-list'),data)
        print(response.data)
        self.assertEqual(response.status_code,401)