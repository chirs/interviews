"""
Chapter 3 | Stacks and Queues
"""


# 3.1 
# Describe how you could use a single array to implement three stacks.




# 3.2
# Design a stack which, in addition to push and pop, also has a function min which returns the minimum element. Push, pop and min should all operate in O(1) time.

class StackException(Exception): pass

class Stack(object):
    """
    A normal stack.
    """
    
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            return StackException("Stack is empty")

    def peek(self):
        e = self.pop()
        self.push(e)
        return e


class MinStack(Stack):
    """
    A stack that keeps track of minimums.
    """

    def __init__(self):
        super(MinStack, self).__init__()
        self.min_stack = Stack()

    def push(self, e):
        if e < self.min_stack.peek():
            self.min_stack.push(e)

        return super(MinStack, self).push(e)

    def pop(self):
        # Something is broken here.
        e = super(MinStack, self).pop()
        if e == self.min_stack.peek():
            self.min_stack.pop()


    @property
    def min(self):
        minimum = self.min_stack.peek()
        self.min_stack.push(minimum)
        return minimum

