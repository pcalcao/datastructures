#!/etc/python

from binary_tree import BinarySearchTree


class SplayTree():

    def __init__(self, inner_tree=None):
        self._innertree = BinarySearchTree() if not inner_tree else inner_tree

    def __setitem__(self, key, value):
        self._innertree[key] = value
        self.__splay(key)

    def __getitem__(self, key):
        if self._innertree.key != key:
            # upgrade to root
            self.__splay(key)
        return self._innertree[key]

    def __delitem__(self, key):
        self.__splay(key)
        del self._innertree[key]

    def __splay(self, key):
        subtree = self._innertree._getsubtree(key)
        if subtree:
            while not subtree.parent is None:
                if self.__should_zig(subtree):
                    # parent is root
                    self.__zig(subtree)
                elif self.__should_zigzig(subtree):
                    # both element and parent are on the same subtree
                    self.__zigzig(subtree)
                else:
                    # element is one subtree, parent is in another
                    self.__zigzag(subtree)
            self._innertree = subtree

    def __zig(self, subtree):
        parent = subtree.parent
        gparent = subtree.parent.parent
        if gparent and self.__isleftchild(parent):
            gparent.left = subtree
        elif gparent and self.__isrightchild(parent):
            gparent.right = subtree
        # rotate to the right if node is left child
        if self.__isleftchild(subtree):
            rightside = subtree.right
            subtree.right = parent
            parent.parent = subtree
            parent.left = rightside
            subtree.parent = gparent
        # rotate to the left if node is right child
        elif self.__isrightchild(subtree):
            leftside = subtree.left
            subtree.left = parent
            parent.parent = subtree
            parent.right = leftside
            subtree.parent = gparent

    def __zigzig(self, subtree):
        self.__zig(subtree.parent)
        self.__zig(subtree)

    def __zigzag(self, subtree):
        self.__zig(subtree)
        self.__zig(subtree)

    def __should_zig(self, subtree):
        return subtree.parent.parent is None

    def __should_zigzig(self, subtree):
        return self.__bothleft(subtree, subtree.parent) or self.__bothright(subtree, subtree.parent)

    def __isleftchild(self, subtree):
        return subtree.parent.left == subtree

    def __isrightchild(self, subtree):
        return subtree.parent.right == subtree

    def __bothleft(self, subtree1, subtree2):
        return self.__isleftchild(subtree1) and self.__isleftchild(subtree2)

    def __bothright(self, subtree1, subtree2):
        return self.__isrightchild(subtree1) and self.__isrightchild(subtree2)
