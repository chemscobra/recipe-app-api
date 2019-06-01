from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""

        email = "testfrom@app.com"
        password = "TestPass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_with_lowercase(self):
        """Test for verifying the email entered is lowercase"""

        email = "test@DOMINIO.COM"
        user = get_user_model().objects.create_user(email=email, password="test123")

        self.assertEquals(user.email, email.lower())

    def test_user_email_invalid(self):
        """Test for user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_superuser(self):
        """ Test for creating a superuser"""

        user = get_user_model().objects.create_superuser("testfrom@app.com", "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
