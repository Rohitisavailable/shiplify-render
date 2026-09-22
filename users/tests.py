from django.test import TestCase

from .models import Stock


class StockModelTests(TestCase):
	def test_string_representation_handles_nullable_item_name(self):
		stock = Stock.objects.create(category='Packaging', item_name=None, quantity=None)

		self.assertEqual(str(stock), 'Unnamed item 0')


class RegistrationTests(TestCase):
	def test_registered_user_can_log_in_again(self):
		registration = self.client.post('/register/', {
			'username': 'new-viewer',
			'email': 'viewer@example.com',
			'password1': 'Strong-password-123',
			'password2': 'Strong-password-123',
		})

		self.assertRedirects(registration, '/login/')
		self.assertTrue(self.client.login(username='new-viewer', password='Strong-password-123'))
		self.assertEqual(self.client.get('/main/').status_code, 200)
