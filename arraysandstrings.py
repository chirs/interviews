"""
Chapter 1. Arrays and Strings
"""

# 1.1 Impelement an algorithm to determine if a string has all unique characters

def unique(s):
    return len(set(s)) == len(s)

def unique2(s):
    # without additional data structures
    # Not quite sure.
    # would like to sort the list.

def reverse(s):
    s2 = ''
    for char in s:
        s2 = char + s2
    return s2


        
