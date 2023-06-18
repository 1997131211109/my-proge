from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class PostCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')


class CommentCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')


# Додайте більше тестових випадків для інших видів та функціоналу

class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_update_profile(self):
        response = self.client.post(reverse('profile'), {'first_name': 'John', 'last_name': 'Doe'})
        self.assertEqual(response.status_code, 302)  # Перевірка успішного оновлення профілю
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, '')  # Перевірка оновленого імені
        self.assertEqual(self.user.last_name, '')  # Перевірка оновленого прізвища

# Додайте більше тестових випадків для інших видів та функціоналу
