"""
utils.py - Utility functions for general purposes.
"""

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)
