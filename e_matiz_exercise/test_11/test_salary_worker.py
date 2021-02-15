import unittest
from salary_worker import Employee


class TestCaseEmployee(unittest.TestCase):
    def setUp(self):
        self.my_worker = Employee('name', 'lastname', 2000)
        self.my_worker.salary_year = 5000
        self.my_worker.register_year = 2020

    def test_give_default_raise(self):
        self.my_worker.salary += self.my_worker.salary_year
        self.assertEqual(self.my_worker.salary, 7000)

    def test_give_custom_raise(self):
        self.my_worker.salary = 6000
        self.my_worker.salary += self.my_worker.salary_year
        self.assertEqual(self.my_worker.salary, 11000)

if __name__ == '__main__':
    unittest.main()
