__author__ = 'pcalcao'

import unittest
from binary_search_tree import BinarySearchTree


class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        bTree = BinarySearchTree()
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        bTree = BinarySearchTree()
        bTree[2] = "v2"
        self.assertEqual("v2", bTree[2])

    def test_update_value(self):
        bTree = BinarySearchTree()
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        bTree[1] = "v2"
        self.assertEqual("v2", bTree[1])


    def test_ad_values_left_and_right(self):
        bTree = BinarySearchTree()

        bTree[2] = "root"
        bTree[1] = "left"
        bTree[3] = "right"

        self.assertEqual("root", bTree[2])
        self.assertEqual("left", bTree[1])
        self.assertEqual("right", bTree[3])

        self.assertEqual(bTree, bTree.left.parent)
        self.assertEqual(bTree, bTree.right.parent)

        self.assertEqual(1, bTree.left.key)
        self.assertEqual("left", bTree.left.value)

        self.assertEqual(3, bTree.right.key)
        self.assertEqual("right", bTree.right.value)


    def test_search(self):
        bTree = init_tree((2,1,3),("v1","v2","v3"))
        self.assertEqual(bTree[2], "v1")
        self.assertEqual(bTree[1], "v2")
        self.assertEqual(bTree[3], "v3")
        self.assertIsNone(bTree[4])

    def test_delete(self):
        bTree = BinarySearchTree()
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        del bTree[1]
        self.assertIsNone(bTree[1])
        del bTree[1]
        self.assertIsNone(bTree[1])
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        bTree[4] = "v4"
        bTree[2] = "v2"
        bTree[5] = "v5"

        del bTree[1] #should leave 4 as the root
        self.assertEqual(4, bTree.key)
        self.assertEqual("v4", bTree.value)
        self.assertIsNone(bTree.parent)
        self.assertEqual(2, bTree.left.key)
        self.assertEqual(5, bTree.right.key)

    def test_find_minimum(self):
        bTree = init_tree()
        min = bTree.find_min_key()
        self.assertEqual(1, min)

    def test_traversal(self):
        tree_struct = (4, 2, 1, 3, 6, 5, 7)
        tree_vals = (40, 20, 10, 30, 60, 50, 70)
        bTree = init_tree(tree_struct, tree_vals)
        nodes = tuple(x for x in bTree.traverse())
        self.assertTupleEqual(tree_struct, nodes)

    def test_ordered_traversal(self):
        tree_struct = (4, 2, 1, 3, 6, 5, 7)
        bTree = init_tree(tree_struct, tree_struct)
        nodes = tuple(x for x in bTree.ordered_traverse())
        self.assertTupleEqual((1,2,3,4,5,6,7), nodes)

    def test_find_max(self):
        tree_struct = (4, 2, 1, 3, 6, 5, 7)
        bTree = init_tree(keys=tree_struct, items=tree_struct)
        self.assertEqual(7, bTree.find_max_key())


def init_tree(keys=(2,1,3), items=("v1","v2","v3")):
    bTree = BinarySearchTree()
    for index, val in enumerate(keys):
        bTree[val] = items[index]
    return bTree






