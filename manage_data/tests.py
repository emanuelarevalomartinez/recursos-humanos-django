from django.test import TestCase
from django.urls import reverse
from .views import UploadFile

class TestUploadFileView(TestCase):
    

    def test_view_renders_correct_template(self):
        response = self.client.get(reverse('charge_file'))
        self.assertTemplateUsed(response, 'uploads/charge_data.html')

    def test_view_returns_http_ok(self):
        response = self.client.get(reverse('charge_file'))
        self.assertEqual(response.status_code, 200)