#!/usr/bin/env python3
# -*- coding: utf-8 -*-    
"""
Test module for the min_or_sum function.

Created on 2024-12-13
Author: Omnia
"""

import unittest
from ..min_or_sum import min_or_sum

class TestMinOrSum(unittest.TestCase):
    """Test suite for the min_or_sum function."""

    def test_minimal_input(self):
        """Test with both inputs as zero."""
        self.assertEqual(min_or_sum(0, 0), 0)

    def test_smaller_value(self):
        """Test when one number is smaller than the other."""
        self.assertEqual(min_or_sum(2, 15), 2)

    def test_equal_values(self):
        """Test when both numbers are equal."""
        self.assertEqual(min_or_sum(11, 11), 22)

    def test_negative_numbers(self):
        """Test with two negative numbers to ensure correct comparison."""
        self.assertEqual(min_or_sum(-6, -60), -60)

    def test_large_numbers(self):
        """Test large integer inputs to check scalability."""
        self.assertEqual(min_or_sum(10**9, 10**10), 10**9)

    def test_float_input(self):
        """Check that non-integer input raises AssertionError."""
        with self.assertRaises(AssertionError):
            min_or_sum(5.7, 5)

    def test_string_input(self):
        """Check that a string input raises AssertionError."""
        with self.assertRaises(AssertionError):
            min_or_sum(5, "5")

if __name__ == '__main__':
    unittest.main()
