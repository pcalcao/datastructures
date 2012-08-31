#!/etc/python

class BinaryTree():
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def put(self, value):
        if self.root is None:
            self.root = value
        elif value < self.root:
            if self.left is None:
                self.left = BinaryTree()
            self.left.put(value)
        elif value > self.root:
            self.right = BinaryTree()
            self.right.put(value)








