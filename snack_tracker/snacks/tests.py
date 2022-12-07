from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

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


    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test')

        self.snack=Snack.objects.create(
            name='test1',
            desc="mohammad",
            purchaser=self.user 
        )


    def test_str_method(self):
        self.assertEqual(str(self.snack),'test1')    

    def test_detail_view(self):
        url = reverse('detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')
    
