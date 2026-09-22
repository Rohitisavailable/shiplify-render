from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Courier


class CourierPageTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='viewer',
			password='test-password-123',
		)
		Courier.objects.create(
			name='Rohit Mahajan',
			service='Amazon',
			package_no='31',
			date_recieved='25/03/2025',
		)
		Courier.objects.create(
			name='Samruddhi',
			service='Meesho',
			package_no='35',
			date_recieved='20/03/2024',
		)

	def test_home_is_public_and_login_is_separate(self):
		home_response = self.client.get('/')

		self.assertEqual(home_response.status_code, 200)
		self.assertContains(home_response, 'Shipping that keeps its')
		self.assertContains(home_response, 'https://github.com/Rohitisavailable')
		self.assertContains(home_response, 'href="/main/"')
		self.assertContains(home_response, 'href="/upcoming/"')
		self.assertContains(home_response, 'Sign in to Shiplify')
		self.assertEqual(self.client.get('/login/').status_code, 200)

		self.client.force_login(self.user)
		authenticated_home = self.client.get('/')
		self.assertNotContains(authenticated_home, 'Sign in to Shiplify')

	def test_dashboard_requires_authentication(self):
		response = self.client.get('/main/')

		self.assertRedirects(response, '/login/?next=/main/')

	def test_logout_redirects_to_public_home(self):
		self.client.force_login(self.user)

		response = self.client.post('/logout/')

		self.assertRedirects(response, '/')
		self.assertFalse(response.wsgi_request.user.is_authenticated)

	def test_dashboard_search_filters_by_package_number(self):
		self.client.force_login(self.user)

		response = self.client.get('/main/?q=31')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Rohit Mahajan')
		self.assertNotContains(response, 'Samruddhi')
