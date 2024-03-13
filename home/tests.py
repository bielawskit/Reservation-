from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_template_contains_(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
        self.assertContains(response, "Rezerwacja")
        self.assertNotContains(response, "Witaj")

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home:home"))
        self.assertEqual(response.status_code, 200)
