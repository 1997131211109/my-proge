from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User



class SignUpViewTest(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)  # Перевірка успішного отримання сторінки реєстрації

    # Додайте інші тести для SignUpView, якщо потрібно


class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Перевірка успішного отримання сторінки профілю

    # Додайте інші тести для profile, якщо потрібно


class CreatePostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_post_view(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)  # Перевірка успішного отримання сторінки створення поста

    # Додайте інші тести для create_post, якщо потрібно


class CreateCommentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')



    # Додайте інші тести для create_comment, якщо потрібно



