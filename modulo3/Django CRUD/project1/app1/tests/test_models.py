from django.test import TestCase

from app1.models import User

class StrTest(TestCase):
    def setUp(self):
        self.user = User(nome="Lucas", telefone=32999,email="lucas@igti.com.br")
    
    def test_str(self):
        self.assertEqual(str(self.user), "Nome:Lucas, Telefone:32999, Email:lucas@igti.com.br")