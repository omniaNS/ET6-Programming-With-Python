#!/usr/bin/env python3
# -*- coding: utf-8 -*-    
"""
Test module for the generate_sequence function.

Created on 2024-12-16
Author: Omnia
"""

import unittest
from ..generate_sequence import generate_sequence

class TestGenerateSequence(unittest.TestCase):
    """Test suite for the generate_sequence function."""

    # Standard Tests
    def test_minimal_input(self):
        """Test when input length is zero."""
        self.assertEqual(generate_sequence(0), [])
        
    def test_positive_small_input(self):
        """Test generating a sequence with a small positive integer."""
        self.assertEqual(generate_sequence(3), [0, 1, 2])

    def test_large_input(self):
        """Test generating a sequence with a large positive integer."""
        self.assertEqual(generate_sequence(10000), list(range(10000)))

    # Defensive Tests
    def test_non_integer_input(self):
        """Test that a non-integer input raises AssertionError."""
        with self.assertRaises(AssertionError):
            generate_sequence("10") 

    def test_negative_input(self):
        """Test that a negative integer input raises AssertionError."""
        with self.assertRaises(AssertionError):
            generate_sequence(-4) 


if __name__ == "__main__":
    unittest.main()
