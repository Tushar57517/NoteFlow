from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your tests here.
class RegisterViewTest(TestCase):
    
    def test_register_template_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        response = self.client.post(reverse("register"), {
            "username": "testuser",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })

        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username="testuser").exists())

        self.assertEqual(response.status_code, 302)