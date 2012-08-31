__author__ = 'pcalcao'

import unittest
from binary_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        bTree = BinarySearchTree()
        bTree.put(1)
        self.assertEqual(1, bTree.root)
        bTree = BinarySearchTree()
        bTree.put(2)
        self.assertEqual(2, bTree.root)

    def test_ad_values_left_and_right(self):
        bTree = BinarySearchTree()
        bTree.put(2)
        self.assertEqual(2, bTree.root)
        bTree.put(1)
        self.assertEqual(1, bTree.left.root)
        self.assertEqual(bTree, bTree.left.parent)
        bTree.put(3)
        self.assertEqual(3, bTree.right.root)
        self.assertEqual(bTree, bTree.right.parent)


    def test_search(self):
        bTree = BinarySearchTree()
        bTree.put(2)
        bTree.put(1)
        bTree.put(3)

        self.assertEqual(bTree.search(2), bTree)
        self.assertEqual(bTree.search(1), bTree.left)
        self.assertEqual(bTree.search(3), bTree.right)

        self.assertIsNone(bTree.search(4))





