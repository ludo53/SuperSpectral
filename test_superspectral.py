# test_superspectral.py
"""
Tests for SuperSpectral module.
"""

import unittest
from superspectral import SuperSpectral

class TestSuperSpectral(unittest.TestCase):
    """Test cases for SuperSpectral class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SuperSpectral()
        self.assertIsInstance(instance, SuperSpectral)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SuperSpectral()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
