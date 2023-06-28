"""
Test for models

"""

from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """"Test creating a user with an email successful"""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        



# Generate a function to add two numbers

