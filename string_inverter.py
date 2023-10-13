#!/usr/bin/python
"""
Showcases simple string invertion
"""

def invert(input):
    """A function to invert the given string"""
    inverted = ''
    if input:
        inverted = input[::-1]
    return inverted