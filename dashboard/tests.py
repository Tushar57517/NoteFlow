from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class DashboardTestView(TestCase):

    def test_dashboard_template_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')