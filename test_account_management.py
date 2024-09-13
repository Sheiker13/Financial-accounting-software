import unittest
from models.account import Account
from unittest.mock import patch

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account('account_id', 'Main Account', 'USD', 1000)

    def test_add_income(self):
        self.account.add_income(500)
        self.assertEqual(self.account.balance, 1500)

    def test_add_expense(self):
        self.account.add_expense(300)
        self.assertEqual(self.account.balance, 700)

    def test_transfer(self):
        other_account = Account('account_2', 'Savings Account', 'USD', 500)
        self.account.transfer(other_account, 200)
        self.assertEqual(self.account.balance, 800)
        self.assertEqual(other_account.balance, 700)

if __name__ == '__main__':
    unittest.main()
