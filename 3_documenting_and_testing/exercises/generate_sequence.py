#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to generate a sequence of non-negative integers.

Created on 2024-12-16
Author: Omnia
"""

def generate_sequence(length: int) -> list[int]:
    """
    Generates a list of non-negative integers from 0 up to length - 1.

    Parameters:
        length (int): The number of integers to generate.

    Returns:
        list[int]: A list of non-negative integers from 0 to length - 1.
    
    Raises:
        AssertionError: If length is not an integer or is negative.

    Examples:
        >>> generate_sequence(0)
        []
        >>> generate_sequence(3)
        [0, 1, 2]
        >>> generate_sequence(1)
        [0]
    """
    # Ensure input is a non-negative integer
    assert isinstance(length, int), "Input must be an integer"
    assert length >= 0, "Input must be non-negative"
    
    # Initialize an empty list to store the generated sequence
    sequence = []
    
    # Initialize a counter to track current number
    counter = 0
    
    # Append numbers to the list until its length matches the input length
    while len(sequence) < length:
        sequence.append(counter)
        counter += 1  

    return sequence
