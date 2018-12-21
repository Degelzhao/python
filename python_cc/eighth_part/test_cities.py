import unittest
from eighth_part.city_functions import city_country


class test_city_country(unittest.TestCase):
    """测试city_country.py"""

    def test_city_country_name(self):
        """能够正确处理像xian,China这样的名字吗"""
        formatted_name = city_country('xian', 'China')
        self.assertEqual(formatted_name, 'xian,China - population ')

class test_city_country_population(unittest.TestCase):
    """测试city_country.py"""

    def test_c_c_p(self):
        """能够处理这种名字吗"""
        formatted_name = city_country('baoji', 'China', population_number = 5000)
        self.assertEqual(formatted_name, 'baoji,China - population 5000')

if __name__ == '__main__':
    unittest.main()