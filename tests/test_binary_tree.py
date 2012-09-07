__author__ = 'pcalcao'

import unittest
from binary_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        bTree = BinarySearchTree()
        bTree.put(1)
        self.assertEqual(1, bTree.key)
        bTree = BinarySearchTree()
        bTree.put(2)
        self.assertEqual(2, bTree.key)

#    def test_ad_values_left_and_right(self):
#        bTree = BinarySearchTree()
#        bTree.put(2)
#        self.assertEqual(2, bTree.key)
#        bTree.put(1)
#        self.assertEqual(1, bTree.left.key)
#        self.assertEqual(bTree, bTree.left.parent)
#        bTree.put(3)
#        self.assertEqual(3, bTree.right.key)
#        self.assertEqual(bTree, bTree.right.parent)
#        bTree.put(5)
#        self.assertEqual(5, bTree.right.right.key)
#
#
#    def test_search(self):
#        bTree = init_tree()
#        self.assertEqual(bTree.search(2), bTree)
#        self.assertEqual(bTree.search(1), bTree.left)
#        self.assertEqual(bTree.search(1).parent, bTree)
#        self.assertEqual(bTree.search(3), bTree.right)
#        self.assertEqual(bTree.search(3).parent, bTree)
#        self.assertIsNone(bTree.search(4))
#
#
#    def test_delete_left(self):
#        bTree = init_tree()
#        self.assertEqual(bTree.search(1), bTree.left)
#        bTree.delete(1)
#        self.assertIsNone(bTree.search(1))
#
#    def test_delete_right(self):
#        bTree = init_tree()
#        self.assertEqual(bTree.search(3), bTree.right)
#        bTree.delete(3)
#        self.assertIsNone(bTree.search(3))
#
#    def test_find_minimum(self):
#        bTree = init_tree()
#        min = bTree.find_minimum()
#        self.assertEqual(1, min.key)
#
#
#    def test_delete_root_one_child(self):
#        bTree = init_tree((3,5,4,6))
#        bTree.delete(3)
#        self.assertEqual(5, bTree.key)
#        self.assertEqual(6, bTree.right.key)
#        bTree = init_tree((4,2,3,1))
#        bTree.delete(4)
#        self.assertEqual(2, bTree.key)
#        self.assertEqual(3, bTree.right.key)
#        self.assertEqual(1, bTree.left.key)
#
#    def test_delete_root(self):
#        bTree = init_tree((3,1,5,4,6))
#        bTree.delete(3) #deleting a node with two children
#        self.assertEqual(4, bTree.key)
#        self.assertEqual(5, bTree.right.key)
#        self.assertEqual(6, bTree.right.right.key)
#        self.assertIsNone(bTree.right.left)
#
#    def test_traversal(self):
#        tree_struct = (4, 2, 1, 3, 6, 5, 7)
#        bTree = init_tree(tree_struct)
#        nodes = tuple(x for x in bTree.traverse())
#        self.assertTupleEqual(tree_struct, nodes)
#
#
#    def test_ordered_traversal(self):
#        tree_struct = (4, 2, 1, 3, 6, 5, 7)
#        bTree = init_tree(tree_struct)
#        nodes = tuple(x for x in bTree.ordered_traverse())
#        self.assertTupleEqual((1,2,3,4,5,6,7), nodes)
#
#    def test_find_max(self):
#        tree_struct = (4, 2, 1, 3, 6, 5, 7)
#        bTree = init_tree(tree_struct)
#        self.assertEqual(7, bTree.find_maximum().key)






def init_tree(values=(2,1,3)):
    bTree = BinarySearchTree()
    for val in values:
        bTree.put(val)
    return bTree






