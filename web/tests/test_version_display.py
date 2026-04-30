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
        # Mark email as verified so the user isn't redirected
        self.user.emailaddress_set.create(
            email="test@test.com",
            verified=True,
            primary=True
        )

    def test_version_visible_in_sidebar(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/cves/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "OPENCVE_VERSION")