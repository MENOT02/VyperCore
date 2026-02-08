# test_vypercore.py
"""
Tests for VyperCore module.
"""

import unittest
from vypercore import VyperCore

class TestVyperCore(unittest.TestCase):
    """Test cases for VyperCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VyperCore()
        self.assertIsInstance(instance, VyperCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VyperCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
