#!/etc/python

from binary_tree import BinarySearchTree

class SplayTree():

    def __init__(self, inner_tree=None):
        self._innertree = BinarySearchTree() if not inner_tree else inner_tree

    def __setitem__(self, key, value):
        self._innertree[key] = value

    def __getitem__(self, key):
        return self._innertree[key]

    def __delitem__(self, key):
        del self._innertree[key]

    def splay(self, key):
        if self._innertree.parent:
            if not self._innertree.parent.parent:
                #zig
                pass

