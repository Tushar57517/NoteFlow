from django.test import TestCase
from django.urls import reverse
from .models import Page
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.
class PageViewTest(TestCase):
    def test_page_template_loads(self):
        user = User.objects.create_user(username="testuser", password="Admin@123")
        page = Page.objects.create(title="first Page", content="test content", owner=user)
        response = self.client.get(reverse('page-view', args=[page.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/page.html')