#!/etc/python

class BinarySearchTree():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None

    def put(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree()
                self.left.parent = self
            self.left.put(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree()
                self.right.parent = self
            self.right.put(value)

    def search(self, value):
        if value  == self.value:
            return self

        if value < self.value and self.left is not None:
            return self.left.search(value)

        if value > self.value and self.right is not None:
            return self.right.search(value)

        return None

    def delete(self, value):
        """
        Base cases are:
         Deleting a leaf - trivial
         Deleting a node with one child only - switch the value with the child
         Deleting a node with two children - find the minimum value on the right subtree and swap the value, deleting that node
        """

        if self.value == value:
            #If I'm a leaf and you want to delete me (shame on you)
            if self.is_leaf():
                if self.parent.value < self.value: #I'm the right node
                    self.parent.right = None
                    self.parent = None
                elif self.parent.value > self.value: #I'm the left node
                    self.parent.left = None
                    self.parent = None
            else:
                if self.left is None:
                    self.right.parent = None
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                elif self.right is None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                    self.left.parent = None
                else: #both children
                    minimum = self.right.find_minimum()
                    min_parent = minimum.parent
                    min_parent.left = None
                    minimum.parent = None
                    self.value = minimum.value

        elif value > self.value and self.right is not None:
            self.right.delete(value)
        elif  value < self.value and self.left is not None:
            self.left.delete(value)



    def is_leaf(self):
        return self.left is None and self.right is None

    def find_minimum(self):
        if self.is_leaf() or self.left is None:
            return self
        return self.left.find_minimum()

    def find_maximum(self):
        if self.is_leaf() or self.right is None:
            return self
        return self.right.find_maximum()

    def traverse(self):
        """
        Traversal of the tree should return a list of values in an order such that, if they are inserted in that same order
        into a new tree, the result has the exact same structure
        """
        yield self.value
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
        yield self.value
        if self.right is not None:
            for x in self.right.ordered_traverse():
                yield x











