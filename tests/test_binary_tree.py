__author__ = 'pcalcao'

import unittest
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        bTree = BinaryTree()
        bTree.put(1)
        self.assertEqual(1, bTree.root)
        bTree = BinaryTree()
        bTree.put(2)
        self.assertEqual(2, bTree.root)

    def test_ad_values_left_and_right(self):
        bTree = BinaryTree()
        bTree.put(2)
        self.assertEqual(2, bTree.root)
        bTree.put(1)
        self.assertEqual(1, bTree.left.root)
        bTree.put(3)
        self.assertEqual(3, bTree.right.root)




