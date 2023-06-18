from django.test import TestCase
from .models import Comment
from .forms import CommentForm


class CommentFormTest(TestCase):
    def test_form_fields(self):
        form = CommentForm()
        expected_fields = ['name', 'email', 'body']
        self.assertEqual(list(form.fields), expected_fields)

    def test_form_valid_data(self):
        form = CommentForm(data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'body': 'This is a test comment'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = CommentForm(data={
            'name': '',  # Empty name
            'email': 'john@example.com',
            'body': 'This is a test comment'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertIn('name', form.errors)

