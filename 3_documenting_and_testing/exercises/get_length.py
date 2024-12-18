#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function that finds the length of iterables.

Created on 2024-12-11
Author: Omnia
"""

from typing import Any

def get_length(iterable: Any) -> int:
    """
    Returns the length of the given iterable if it's non-empty, otherwise returns None.

    Parameters:
        iterable (Any): An iterable object such as a string, list, tuple, or dictionary.

    Returns:
        int: Length of the iterable if it's not empty, otherwise None.

    Raises:
        AssertionError: If input is not an iterable.

    Examples:
        >>> get_length([2, 3, 'i'])
        3
        >>> get_length('example')
        7
        >>> get_length(())
        None
    """
    # Defensive assertion: Ensure the input is an iterable.
    assert hasattr(iterable, '__iter__'), "Input must be an iterable"

    # Check if the iterable is empty
    if len(iterable) == 0:
        return None
    
    # Return the length of the non-empty iterable
    return len(iterable)
