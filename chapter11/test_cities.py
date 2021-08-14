import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):

	def test_city_country(self):
		right_type = city_country('beijing', 'china')
		self.assertEqual(right_type, 'Beijing, China')

	def test_city_country_population(self):
		right_type = city_country('beijing', 'china',2850000)
		self.assertEqual(right_type, 'Beijing, China - Population 2850000')

if __name__ =='__main__':
	unittest.main()
