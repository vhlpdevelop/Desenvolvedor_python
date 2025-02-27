from django.test import TestCase

# Create your tests here.

def add_num(num):
    return num+1

class SimpleTestCase(TestCase):
    def setUp(self):
        self.num = 1

    def test_add_num(self):
        valor = add_num(self.num)
        self.assertTrue(valor == 2)

