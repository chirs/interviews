"""
Chapter 7 | Mathematics and Probability
"""

# 7.1 
# You have a basketball hoop and someone says that you can play one of two games.
# Game 1: You get one shot to make the hoop.
# Game 2: You get three shots and you have to make two of three shots.
# If p is the probability of making a particular shot, for which values of p should
# you pick one game over the other?

# Probability of winning game #1 is p.
# Probability of winning game # 2 is probablity of making a) three consecutive shots
# plus the probability of making b) two of three shots.
# probability a. is p^3.
# probability b. is 6(p^2)(1-p)
# solve p == p^3 + 6(p^2)(1-p)
# p == p^3 + 6(p^2) - 6p^3
# 5p^3 - 6p^2 == 0
# p(5p - 6) == 

# Nope.

def p2(p):
    return 1 - ()


# 7.4 implement multiply, subtract, divide with only addition


def multiply(a, b):
    i = 0
    product = 0

    if b < 0:
        return product
        #while i > b:
            # Impossible?
        #    pass

    elif b > 0:
        while i < b:
            i += 1
            product += b
    
    else:
        return product

def subtract(a, b):
    pass


