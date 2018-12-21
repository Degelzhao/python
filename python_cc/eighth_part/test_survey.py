import unittest
from eighth_part.employees import Employee

class TestEmployeeSurvey(unittest.TestCase):

    def setUp(self):
        first_name = 'Aiolos'
        last_name = 'Zhao'
        annual_salary = 100000
        self.employee = Employee(first_name, last_name, annual_salary)

    def test_give_default_raise(self):
        money = self.employee.give_raise()
        self.assertEqual(105000, money)

    def test_give_custom_raise(self):
        money = self.employee.give_raise(10000)
        self.assertEqual(110000, money)

if __name__ == '__main__':
    unittest.main()