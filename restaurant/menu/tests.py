from django.test import TestCase

# Create your tests here.

# tests for menu
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class MenuTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.menu = Menu.objects.create(name='test menu', price=10, date='2022-01-01')

    def test_menu_list(self):
        response = self.client.get(reverse('menu:menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test menu')
