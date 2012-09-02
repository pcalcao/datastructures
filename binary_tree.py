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
            self.left.put(value)
            self.left.parent = self
        elif value > self.value:
            self.right = BinarySearchTree()
            self.right.put(value)
            self.right.parent = self

    def search(self, value):
        if value  == self.value:
            return self

        if value < self.value and self.left is not None:
            return self.left.search(value)

        if value > self.value and self.right is not None:
            return self.right.search(value)

        return None

    def delete(self, value):
        #If I'm a leaf and you want to delete me (shame on you)
        if self.value == value and self.is_leaf():
            if self.parent.value < self.value: #I'm the right node
                self.parent.right = None
                self.parent = None
            elif self.parent.value > self.value: #I'm the left node
                self.parent.left = None
                self.parent = None
        elif value > self.value and self.right is not None:
            self.right.delete(value)
        elif  value < self.value and self.left is not None:
            self.left.delete(value)
        elif self.value == value: #I am root of a tree, and I am to be deleted
            #find mininum on right side and switch value, clearing that node
            self.value = self.right.value



    def is_leaf(self):
        return self.left is None and self.right is None









