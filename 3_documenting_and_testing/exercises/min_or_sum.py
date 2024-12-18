#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function that returns the minimum of two numbers or their sum if they are equal.

Created on 2024-12-13
Author: Omnia
"""

def min_or_sum(first_num: int, second_num: int) -> int:
    """
    Returns the smaller number between two integers or their sum if they are equal.

    Parameters:
        first_num (int): The first integer.
        second_num (int): The second integer.

    Returns:
        int: The smaller number or the sum if they are equal.

    Raises:
        AssertionError: If either input is not an integer.

    Examples:
        >>> min_or_sum(2, 3)
        2
        >>> min_or_sum(4, 4)
        8
        >>> min_or_sum(-3, 0)
        -3
    """
    # Ensure both inputs are integers
    assert isinstance(first_num, int), "First number must be an integer"
    assert isinstance(second_num, int), "Second number must be an integer"

    # Check which number is smaller and return it
    if first_num < second_num:
        return first_num
    elif first_num > second_num:
        return second_num
    
    # If both numbers are equal, return their sum
    else:
        return first_num + second_num
