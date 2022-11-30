from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnackTests(TestCase):
    def test_home_page_status(self):
        url = reverse('snack')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')
