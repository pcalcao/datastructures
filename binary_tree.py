#!/etc/python

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        self.parent = None

    def put(self, value):
        if self.root is None:
            self.root = value
        elif value < self.root:
            if self.left is None:
                self.left = BinarySearchTree()
            self.left.put(value)
            self.left.parent = self
        elif value > self.root:
            self.right = BinarySearchTree()
            self.right.put(value)
            self.right.parent = self

    def search(self, value):
        if value  == self.root:
            return self

        if value < self.root and self.left is not None:
            return self.left.search(value)

        if value > self.root and self.right is not None:
            return self.right.search(value)

        return None

    def delete(self, value):
        pass









