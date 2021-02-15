import unittest
from city_country import get_city_country as gcc

class CityTestCase(unittest.TestCase):
    def test1_city_country(self):
        word = gcc('Kyiv', 'Ukraine')
        self.assertEqual(word, 'Kyiv Ukraine')


# unittest.main()

if __name__ == '__main__':
    unittest.main()
