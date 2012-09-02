__author__ = 'pcalcao'

import unittest
from binary_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        bTree = BinarySearchTree()
        bTree.put(1)
        self.assertEqual(1, bTree.value)
        bTree = BinarySearchTree()
        bTree.put(2)
        self.assertEqual(2, bTree.value)

    def test_ad_values_left_and_right(self):
        bTree = BinarySearchTree()
        bTree.put(2)
        self.assertEqual(2, bTree.value)
        bTree.put(1)
        self.assertEqual(1, bTree.left.value)
        self.assertEqual(bTree, bTree.left.parent)
        bTree.put(3)
        self.assertEqual(3, bTree.right.value)
        self.assertEqual(bTree, bTree.right.parent)


    def test_search(self):
        bTree = init_tree()
        self.assertEqual(bTree.search(2), bTree)
        self.assertEqual(bTree.search(1), bTree.left)
        self.assertEqual(bTree.search(1).parent, bTree)
        self.assertEqual(bTree.search(3), bTree.right)
        self.assertEqual(bTree.search(3).parent, bTree)
        self.assertIsNone(bTree.search(4))


    def test_delete_left(self):
        bTree = init_tree()
        self.assertEqual(bTree.search(1), bTree.left)
        bTree.delete(1)
        self.assertIsNone(bTree.search(1))

    def test_delete_right(self):
        bTree = init_tree()
        self.assertEqual(bTree.search(3), bTree.right)
        bTree.delete(3)
        self.assertIsNone(bTree.search(3))

    def test_delete_root(self):
        bTree = init_tree()
        self.assertEqual(bTree.search(2), bTree)
        bTree.delete(2)
        self.assertEqual(bTree.value, 3)
        self.assertEqual(bTree.left, bTree.search(1))
        self.assertIsNone(bTree.right)

def init_tree():
    bTree = BinarySearchTree()
    bTree.put(2)
    bTree.put(1)
    bTree.put(3)
    return bTree






