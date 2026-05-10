from django.test import TestCase
from .models import User
from django.urls import reverse
from .views import AdminSession
# Create your tests here.


class UserTest(TestCase):
    
    def test_mi_modelo_crea_instancia_correctamente(self):
        # Configuración inicial
        instance = User()
        
        # Verificar
        self.assertIsInstance(instance, User)



class TestAdminSession(TestCase):


    def test_view_renders_correct_template(self):
        response = self.client.get(reverse('admin_session'))
        self.assertTemplateUsed(response, 'admin/admin_session.html')

    def test_view_returns_http_ok(self):
        response = self.client.get(reverse('admin_session'))
        self.assertEqual(response.status_code, 200)