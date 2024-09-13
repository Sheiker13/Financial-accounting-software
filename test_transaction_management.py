import unittest
from models.transaction import Transaction
from unittest.mock import patch
from datetime import datetime

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction('trans_id', 'account_id', 500, 'income', datetime.now())

    @patch('utils.file_handler.save_data')
    def test_record_transaction(self, mock_save):
        self.transaction.record_transaction()
        mock_save.assert_called_once()

    def test_transaction_data(self):
        self.assertEqual(self.transaction.amount, 500)
        self.assertEqual(self.transaction.transaction_type, 'income')

if __name__ == '__main__':
    unittest.main()
