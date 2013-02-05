#!/etc/python

from binary_tree import BinarySearchTree

class SplayTree():

    def __init__(self, inner_tree=None):
        self._innertree = BinarySearchTree() if not inner_tree else inner_tree

    def __setitem__(self, key, value):
        self._innertree[key] = value

    def __getitem__(self, key):
        if self._innertree.key != key:
            #upgrade to root
            self.__splay(key)
        return self._innertree[key]

    def __delitem__(self, key):
        del self._innertree[key]

    def __splay(self, key):
        print key
        subtree = self._innertree._getsubtree(key)
        print subtree.parent
        print subtree.parent.parent
        if not subtree.parent.parent:
            self.zig(key)

    def zig(self, key):
        pass

    def zigzig(self, key):
        pass

    def zigzag(self, key):
        pass

