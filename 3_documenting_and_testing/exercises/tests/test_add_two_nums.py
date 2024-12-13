#!/usr/bin/env python3
# -*- coding: utf-8 -*-    
"""
Test module for the add_two_nums function.

Created on 2024-12-11
Author: Omnia
"""
import unittest

from ..add_two_nums import add_two_nums

class TestAddTwoNums(unittest.TestCase):
    """Test suite for the add_two_nums function"""
    
    #Standard test cases
    def test_positive_ints(self):
        """test adding two positive numbers"""
        self.assertEqual(add_two_nums(23,99), 122)
        
    def test_negative_ints(self):
        """test adding two negative numbers"""
        self.assertEqual(add_two_nums(-22,-13), -35)
        
    def test_zero(self):
        """test adding zero"""
        self.assertEqual(add_two_nums(0,0),0)
    
    #defensive cases 
    def test_not_int(self):
        """Should raise AssertionError for non-int input"""
        with self.assertRaises(AssertionError):
            add_two_nums(1.2,3)
    

if __name__ == '__main__':
    unittest.main()
