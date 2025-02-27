from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from app1.models import User

class ViewTest(TestCase):
    def setUp(self):
        self.dados = {
            'nome':'nome',
            'telefone':329999,
            'email':'email'
        }

        self.client = Client()
    def test_index(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEqual(request.status_code, 200)
    
    def test_createuser(self):
        request = self.client.post(reverse_lazy('createuser'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    def test_modificar(self):
        request = self.client.post(reverse_lazy('modificar'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    def test_deleteuser(self):
        request = self.client.post(reverse_lazy('deleteuser'), data=self.dados)
        self.assertEqual(request.status_code, 302)