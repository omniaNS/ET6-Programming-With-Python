#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the is_in function
Created on 2024-12-18
Author: Omnia
"""

import unittest
from ..is_in import is_in

class TestIsIn(unittest.TestCase):
    """Test Suite for the is_in function"""

    def test_minimal_input(self):
        """Test when item is empty string and both lists are empty"""
        self.assertEqual(is_in('', [],  []), False)
        
    def test_str_is_in_first_list(self):
        """Test when item is found in the first list"""
        self.assertEqual(is_in('a', ['a','b','c'],  ['d','e']), True)

    def test_str_is_in_second_list(self):
        """Test when item is found in the second list"""
        self.assertEqual(is_in('1', ['11','12'],  ['1','2']), True)
        
    def test_str_is_not_in_lists(self):
        """Test when item is not found in the lists"""
        self.assertEqual(is_in('x', ['a','b'],  ['d','e']), False)

    def test_case_sensitive_str(self):
        """Test when item is not found because case sensitivity"""
        self.assertEqual(is_in('Apple', ['apple','banana'],  ['Cherry']), False)

    

    #defensive tests
    def test_invalid_first_input(self):
        """should raise assertion error because first parameter is not a string"""
        with self.assertRaises(AssertionError):
            is_in(12, [12,'12'],  ['1','2'])

    def test_invalid_second_input(self):
        """should raise assertion error because second parameter is not a list"""
        with self.assertRaises(AssertionError):
            is_in('12', '12',  ['1','2'])

    def test_invalid_third_input(self):
        """should raise assertion error because third parameter is not a list of strings"""
        with self.assertRaises(AssertionError):
            is_in('12', ['12'],  [1, 2])

if __name__ == '__main__':
    unittest.main()
