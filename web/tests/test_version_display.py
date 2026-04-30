# tests for first group issue 655 by Matt Kustigian
from pathlib import Path

from django.test import TestCase, override_settings
from django.urls import reverse

from organizations.models import Membership, Organization
from users.models import User


@override_settings(ENABLE_ONBOARDING=False)
class VersionDisplayTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@test.com",
        )
        self.user.emailaddress_set.create(
            email="test@test.com",
            verified=True,
            primary=True,
        )

    def test_version_visible_in_sidebar(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(reverse("cves"))
        self.assertEqual(response.status_code, 200)

        expected_version = response.context["OPENCVE_VERSION"]
        self.assertContains(response, f"v{expected_version}")
