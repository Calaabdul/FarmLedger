from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Produce


class ProduceTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='farmer1',
            password='testpassword123'
        )

        self.other_user = User.objects.create_user(
            username='farmer2',
            password='testpassword123'
        )

        self.produce = Produce.objects.create(
            owner=self.other_user,
            name='Maize',
            quantity=50,
            unit='kg'
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_access_dashboard(self):
        self.client.login(
            username='farmer1',
            password='testpassword123'
        )

        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 200)

    def test_user_cannot_edit_another_users_record(self):
        self.client.login(
            username='farmer1',
            password='testpassword123'
        )

        response = self.client.get(
            reverse('produce-update', kwargs={'pk': self.produce.pk})
        )

        self.assertEqual(response.status_code, 404)