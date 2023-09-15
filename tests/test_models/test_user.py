#!/usr/bin/python3
"""test for User class"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test  class user methode"""

    @classmethod
    def setUpClass(cls):
        """test class methode"""
        cls.userInstance = User()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """test class methode"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_attrs(self):
        """test attributes with self.assertEqual"""
        self.assertEqual(self.userInstance.email, "")
        self.assertEqual(self.userInstance.password, "")
        self.assertEqual(self.userInstance.first_name, "")
        self.assertEqual(self.userInstance.last_name, "")


if __name__ == "__main__":
    unittest.main()
