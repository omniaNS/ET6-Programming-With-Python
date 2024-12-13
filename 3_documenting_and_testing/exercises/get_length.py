#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function that finds the length of iterables

Created on 2024-12-11
Author: Omnia
"""

def get_length(a):
    """
    takes a string, a list, or a tuple and returns the number of items/characters in the iterable or None if empty
    
    Parameters:
        a: can be a string, a list, a tuple, or a dictionary
        
    Returns:
        int: The length of the iterable if not empty
        None: if the iterable is empty
    
    Raises:
        AssertionError: if input is not a string, a list, a tuple, or a dictionary
    
    Examples:
        >>> get_length([2,3,'i'])
        3
        >>> get_length('example')
        7
        >>> get_length(())
        None
    """
    
    #defensive assertions
    #input should be an iterable type
    assert hasattr(a,'__iter__')
    
    if len(a) == 0:
        return None
    
    return len(a)
