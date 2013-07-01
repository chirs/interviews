"""
Chapter 17 | Moderate
"""

# 17.12
# Design an algorithm to find all pairs of integers within an array
# which sum to a specified value.


def pairs_with_sum(lst, value):
    s = set(lst)
    pairs = set()

    for integer in s:
        pair = value - integer
        if integer in s and pair in s:
            t = tuple(sorted([integer, pair]))
            pairs.add(t)
            
    return sorted(pairs)
            
        


