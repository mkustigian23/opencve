# tests for first group issue 655 by Matt Kustigian
import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class VersionDisplayTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@test.com"
        )

    def test_version_visible_in_sidebar(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/")
        self.assertContains(response, "OPENCVE_VERSION")