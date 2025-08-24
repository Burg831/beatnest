from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Gig

class GigViewsTests(TestCase):
    def setUp(self):
        now = timezone.now()
        for i in range(13):
            Gig.objects.create(
                title=f"Test {i+1}",
                company=f"Test {i+1}",
                location=f"Test {i+1}",
                posted_at=now - timezone.timedelta(minutes=i),
            )
        Gig.objects.create(
            title="DJ COBRA",
            company="Viper Co",
            location="LA",
            posted_at=now,
        )

    def test_list_first_page_has_10(self):
        resp = self.client.get(reverse("gig_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(len(resp.context["page_obj"].object_list), 10)

    def test_search_filters_results(self):
        resp = self.client.get(reverse("gig_list"), {"q": "cobra"})
        self.assertEqual(resp.status_code, 200)
        html = resp.content.decode()
        self.assertIn("DJ COBRA", html)
        self.assertNotIn(">Test 10<", html)

    def test_paging_preserves_q(self):
        resp = self.client.get(reverse("gig_list"), {"q": "Test", "page": 2})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["page_obj"].number, 2)
        html = resp.content.decode()
        self.assertIn("q=Test", html)

