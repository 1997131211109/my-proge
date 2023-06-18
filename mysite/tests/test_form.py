from django.test import TestCase
from django.contrib.auth.models import User
from user_accounts.models import Profile
from blog.models import Post, Comment
from user_accounts.forms import UserProfileForm, PostForm, CommentForm


class UserProfileFormTest(TestCase):
    def test_form_fields(self):
        form = UserProfileForm()
        expected_fields = ['bio', 'date_of_birth', 'first_name', 'last_name', 'email', 'gender']
        self.assertSequenceEqual(list(form.fields.keys()), expected_fields)


class PostFormTest(TestCase):
    def test_form_fields(self):
        form = PostForm()
        expected_fields = ['title', 'content']
        self.assertSequenceEqual(list(form.fields.keys()), expected_fields)


class CommentFormTest(TestCase):
    def test_form_fields(self):
        form = CommentForm()
        expected_fields = ['name', 'email', 'body']
        self.assertSequenceEqual(list(form.fields.keys()), expected_fields)


class ModelFormTest(TestCase):
    def test_user_profile_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        form = UserProfileForm(data={
            'bio': 'Test Bio',
            'date_of_birth': '2000-01-01',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'gender': 'male'
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid_data(self):
        form = UserProfileForm(data={})
        self.assertFalse(form.is_valid())

    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Post',
            'content': 'Lorem ipsum dolor sit amet.'
        })
        self.assertTrue(form.is_valid())

    def test_post_form_invalid_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())

    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'name': 'John Doe',
            'email': 'test@example.com',
            'body': 'Test comment'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
