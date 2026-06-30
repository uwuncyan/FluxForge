# test_fluxforge.py
"""
Tests for FluxForge module.
"""

import unittest
from fluxforge import FluxForge

class TestFluxForge(unittest.TestCase):
    """Test cases for FluxForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxForge()
        self.assertIsInstance(instance, FluxForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
