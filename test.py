import unittest
import datetime
from main import ModernBank

class ModernBankTest(unittest.TestCase):
    def setUp(self):
        self.pb = ModernBank(10000, datetime.date(2023, 12, 31))
        self.pb.deposit(5000)

    def test_show_goal_deadline(self):
        self.assertEqual(self.pb.show_goal_deadline(), None)

    def test_show_balance(self):
        self.assertEqual(self.pb.show_balance(), None)

    def test_show_days_to_goal(self):
        self.assertEqual(self.pb.show_days_to_goal(), None)

    def test_show_months_to_goal(self):
        self.assertEqual(self.pb.show_months_to_goal(), None)

    def test_show_years_to_goal(self):
        self.assertEqual(self.pb.show_years_to_goal(), None)

    def test_show_interest(self):
        self.assertEqual(self.pb.show_interest(), None)

if __name__ == '__main__':
    unittest.main()