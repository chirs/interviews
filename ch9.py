# Python3

"""
Chapter 9 - Recursion and Dynamic Programming
"""

import functools


# 9.1
# A child is running up a staircase with n steps, and can hop
# either 1 step, 2 steps, or 3 steps at a time. Implement a 
# method to count how many possible ways the child can run up
# the stairs.


@functools.lru_cache(maxsize=1024)
def climb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb(n-1) + climb(n-2) + climb(n-3)

    



# 9.8 calculate the number of different ways to 
# represent n cents.

DENOMINATIONS = { 1, 5, 10, 25 }

def change(cents):
    for e in DENOMINATIONS:
        pass


# 9.9 Write an algorithm to print all the ways 
# of arranging eight queens on an 8x8 chess board
# 


from itertools import permutations


QUEENS = 8
cols = range(QUEENS)

def four_queens():
    for vec in permutations(cols):
        if (n == len(set(vec[i] + i for i in cols))
            == len(set(vec[i] - i for i in cols))):
            print(vec)

