#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to add two numbers

Created on 2024-12-11
Author: Omnia
"""

def add_two_nums(a,b):
    """
    Adds two numbers and returns the result
    
    Parameters:
        a (int): The first number
        b (int): The second number
        
    Returns:
        int: The sum of the two numbers
    
    Raises:
        AssertionError: if input is not an integer
    
    Examples:
        >>> add(1,2)
        3
        >>> add(-55,0)
        -55
        >>> add(0,0)
        0
    """
    #defensive assertions
    #both parameters should be integers
    assert isinstance(a,int)
    assert isinstance(b,int)
    return a + b
