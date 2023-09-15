#!/usr/bin/python3
"""State the unittest for State class"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test attributes with correct output"""

    @classmethod
    def setUpClass(cls):
        """Test attributes with correct output"""
        cls.stateInstance = State()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Test attributes with correct output"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_attrs(self):
        """Test attributes with correct output"""
        self.assertEqual(self.stateInstance.name, "")


if __name__ == "__main__":
    unittest.main()
