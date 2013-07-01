"""
Chapter 4 | Trees and Graphs
"""


class Node(object):
    
    def __init__(self, val):
        self._l = None
        self._r = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        root = node
