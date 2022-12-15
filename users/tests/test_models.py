from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegistrationTests(TestCase):
    def setUp(self):
        url = reverse('users:registration_view')
        self.response = self.client.get(url)

    def test_registration_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/registration.html')
        self.assertContains(self.response, 'Rejestracja')
        self.assertNotContains(self.response, 'Login')

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(name='Test', surname='123', email='test@test.pl', password='testpass1')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@test.pl')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_club)

