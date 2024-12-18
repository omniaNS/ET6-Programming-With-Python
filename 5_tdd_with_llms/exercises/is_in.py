#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function that checks if an item exists in at least one of the two lists
Created on 2024-12-18
Author: Omnia
"""

def is_in(item: str, list1: list[str], list2: list[str]) -> bool:
    """
    Checks if the given item exists in at least one of the two lists.
    
    Parameters:
        item (str): The string to search for.
        list1 (list[str]): The first list of strings to search in.
        list2 (list[str]): The second list of strings to search in.

    Returns:
        bool: True if the item is found in at least one of the lists, False otherwise.
    
    Raises:
        AssertionError: If `item` is not a string or if `list1` and `list2` are not lists of strings.

    Examples:
        >>> is_in("apple", ["apple", "banana"], ["cherry", "date"])
        True
        
        >>> is_in("grape", ["apple", "banana"], ["cherry", "date"])
        False
        
        >>> is_in("", ["apple", "banana"], ["", "cherry"])
        True
    """
    # Validate input types
    assert isinstance(item, str), "Item to search for must be a string"
    assert isinstance(list1, list), "First List to search in must be a list of strings"
    assert isinstance(list2, list), "Second List to search in must be a list of strings"
    assert all(isinstance(x, str) for x in list1), "List must only contain strings"
    assert all(isinstance(x, str) for x in list2), "List must only contain strings"
    
    # Return True if item is found in either of the lists, False otherwise
    return item in list1 or item in list2
