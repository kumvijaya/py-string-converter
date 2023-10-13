"""
Unit tests for invert function
"""

from string_inverter import invert

def test_invert_with_value():
    """Test with valid string"""
    assert invert('Hello') == 'olleH'

def test_invert_with_empty():
    """Test with empty string"""
    assert invert('') == ''

def test_invert_with_none():
    """Test with None"""
    assert invert(None) == ''

def test_invert_single_char():
    """Test with single char"""
    assert invert('A') == 'A'
