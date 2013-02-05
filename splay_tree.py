#!/etc/python

class SplayTree():
    def __init__(self, parent=None):
        self.key = None
        self.value = None
        self.left = None
        self.right = None
        self.parent = parent

    def __setitem__(self, key, value):
        if self.key is None:
            self.key = key
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = SplayTree(self)
            self.left.__setitem__(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = SplayTree(self)
            self.right.__setitem__(key, value)
        elif key == self.key:
            self.value = value

    def __getitem__(self, key):
        if key  == self.key:
            return self.value
        if key < self.key and self.left is not None:
            return self.left.__getitem__(key)
        if key > self.key and self.right is not None:
            return self.right.__getitem__(key)
        return None


    def __delitem__(self, key):
        """
        Base cases are:
         Deleting a leaf - trivial
         Deleting a node with one child only - switch the value with the child
         Deleting a node with two children - find the minimum value on the right subtree and swap the value, deleting that node
        """

        if self.key == key:
            #If I'm a leaf and you want to delete me (shame on you)
            if self.is_leaf():
                if self.parent is None: #deleting the root, no children
                    self.key = None
                    self.value = None
                elif self.parent.key > self.key: #I'm the left node
                    self.parent.left = None
                    self.parent = None
                elif  self.parent.key < self.key: #I'm the right node
                    self.parent.right = None
                    self.parent = None
            else:
                if self.left is None:
                    self.right.parent = None
                    self.__copy_node(self.right)
                elif self.right is None:
                    self.left.parent = None
                    self.__copy_node(self.left)
                else: #both children
                    minimum = self.right.find_min_key()
                    min_parent = minimum.parent
                    min_parent.left = None
                    minimum.parent = None
                    self.key = minimum.key

        elif key > self.key and self.right is not None:
            self.right.__delitem__(key)
        elif  key < self.key and self.left is not None:
            self.left.__delitem__(key)

    def is_leaf(self):
        return self.left is None and self.right is None

    def find_min_key(self):
        if self.is_leaf() or self.left is None:
            return self.key
        return self.left.find_min_key()

    def find_max_key(self):
        if self.is_leaf() or self.right is None:
            return self.key
        return self.right.find_max_key()

    def traverse(self):
        """
        Traversal of the tree should return a list of values in an order such that, if they are inserted in that same order
        into a new tree, the result has the exact same structure
        """
        yield self.key
        if self.left is not None:
            for x in self.left.traverse():
                yield x
        if self.right is not None:
            for x in self.right.traverse():
                yield x

    def ordered_traverse(self):
        if self.left is not None:
            for x in self.left.ordered_traverse():
                yield x
        yield self.key
        if self.right is not None:
            for x in self.right.ordered_traverse():
                yield x


    def __copy_node(self, other_node):
        self.key = other_node.key
        self.value = other_node.value
        self.left = other_node.left
        self.right = other_node.right

    def splay(self):
        if self.parent:
            if not self.parent.parent:
                #zig
                
