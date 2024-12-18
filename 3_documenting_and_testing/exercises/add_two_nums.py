#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to add two numbers

Created on 2024-12-11
Author: Omnia
"""

def add_two_nums(first_number: int, second_number: int) -> int:
    """
    Adds two integers and returns the result.

    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The sum of the two numbers.

    Raises:
        AssertionError: If inputs are not integers.

    Assumptions:
        - Both inputs must be integers.

    Examples:
        >>> add_two_nums(1, 2)
        3
        >>> add_two_nums(-55, 0)
        -55
        >>> add_two_nums(0, 0)
        0
    """
    #Ensure both numbers are integers
    assert isinstance(first_number, int), "first_number must be an integer"
    assert isinstance(second_number, int), "second_number must be an integer"
    
    return first_number + second_number
