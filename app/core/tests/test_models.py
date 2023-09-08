"""Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test for Models"""

    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successful"""

        email = "test@example.com"
        password = "password"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
