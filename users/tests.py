from django.test import TestCase

from .models import Stock


class StockModelTests(TestCase):
	def test_string_representation_handles_nullable_item_name(self):
		stock = Stock.objects.create(category='Packaging', item_name=None, quantity=None)

		self.assertEqual(str(stock), 'Unnamed item 0')
