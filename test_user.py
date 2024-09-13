import unittest
from unittest.mock import patch, mock_open
from models.user import User
from utils.file_handler import load_data, save_data

class TestUser(unittest.TestCase):

    @patch('utils.file_handler.load_data', return_value={})
    @patch('utils.file_handler.save_data')
    def test_register(self, mock_save, mock_load):
        user = User('testuser', 'password123', 'testuser@example.com')
        user.register()
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][1]
        self.assertIn('testuser', saved_data)

    @patch('utils.file_handler.load_data', return_value={
        'testuser': {'password': 'password123', 'email': 'testuser@example.com'}
    })
    def test_login_success(self, mock_load):
        self.assertTrue(User.login('testuser', 'password123'))

    @patch('utils.file_handler.load_data', return_value={})
    def test_login_fail(self, mock_load):
        self.assertFalse(User.login('nonexistentuser', 'password123'))

if __name__ == '__main__':
    unittest.main()
