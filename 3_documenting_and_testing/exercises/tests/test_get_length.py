#!/usr/bin/env python3
# -*- coding: utf-8 -*-    
"""
Test module for the get_length function.

Created on 2024-12-11
Author: Omnia
"""
import unittest

from ..get_length import get_length

class TestGetLength(unittest.TestCase):
    """Test suite for the get_length function"""
    
    #Standard test cases
    def test_minimal_list_input(self):
        """test empty list"""
        self.assertEqual(get_length([]), None)

    def test_minimal_string_input(self):
        """test empty string"""
        self.assertEqual(get_length(''), None)
        
    def test_minimal_tuple_input(self):
        """test empty tuple"""
        self.assertEqual(get_length(()), None)
    
    def test_minimal_dictionary_input(self):
        """test empty dictionary"""
        self.assertEqual(get_length({}), None)
            
    def test_non_empty_list(self):
        """test non empty list"""
        self.assertEqual(get_length([23,'',[]]), 3)
        
    def test_non_empty_string(self):
        """test non empty string"""
        self.assertEqual(get_length('this is a string'), 16)
        
    def test_non_empty_tuple(self):
        """test non empty tuple"""
        self.assertEqual(get_length((1,'x')), 2)
        
    def test_non_empty_dictionary(self):
        """test non empty dictionary"""
        self.assertEqual(get_length({"brand": "Ford","model": "Mustang","year": 1964}), 3)

    #Edge Cases
    def test_large_input(self):
        """test very long strings"""
        self.assertEqual(get_length('a' * 10**6), 10**6)
        
    #Defensive tests
    def test_non_iterable_input(self):
        """Should raise AssertionError for non iterable input"""
        with self.assertRaises(AssertionError):
            get_length(123)

if __name__ == '__main__':
    unittest.main()
