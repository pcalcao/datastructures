__author__ = 'pcalcao'

import unittest
from splay_tree import SplayTree


class TestSplayTree(unittest.TestCase):

    def test_creation(self):
        bTree = SplayTree()
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        bTree = SplayTree()
        bTree[2] = "v2"
        self.assertEqual("v2", bTree[2])

    def test_update_value(self):
        bTree = SplayTree()
        bTree[1] = "v1"
        self.assertEqual("v1", bTree[1])
        bTree[1] = "v2"
        self.assertEqual("v2", bTree[1])

    @unittest.skip("Not yet implemented, depends on some sorting stuff out in get")
    def test_search(self):
        bTree = init_tree((2,1,3),("v1","v2","v3"))
        self.assertEqual(bTree[2], "v1")
        self.assertEqual(bTree[1], "v2")
        self.assertEqual(bTree[3], "v3")
        self.assertIsNone(bTree[4])

    @unittest.skip("Not yet implemented, depends on some sorting stuff out in get")
    def test_delete(self):
        bTree = SplayTree()
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

    def test_splay_zig_left_child(self):
        bTree = init_tree()
        val = bTree[1]
        self.assertEqual(1, bTree._innertree.key)
        self.assertEqual(2, bTree._innertree.right.key)
        self.assertIsNone(bTree._innertree.left)
        self.assertIsNone(bTree._innertree.parent)

    def test_splay_zig_right_child(self):
        bTree = init_tree()
        val = bTree[3]
        self.assertEqual(3, bTree._innertree.key)
        self.assertEqual(2, bTree._innertree.left.key)
        self.assertEqual(3, bTree._innertree.left.parent.key)
        self.assertIsNone(bTree._innertree.right)
        self.assertIsNone(bTree._innertree.parent)

    def test_splay_zigzig_left(self):
        bTree = init_tree((4,2,1,3,6,5,7), (4,2,1,3,6,5,7))   
        val = bTree[1] 
        self.assertEqual(1, bTree._innertree.key)

    def test_splay_zigzig_right(self):
        bTree = init_tree((4,2,1,3,6,5,7), (4,2,1,3,6,5,7))   
        val = bTree[7] 
        self.assertEqual(7, bTree._innertree.key)

    def test_splay_zigzag(self):
        bTree = init_tree((4,2,1,3,6,5,7), (4,2,1,3,6,5,7))   
        val = bTree[5]
        self.assertEqual(5, bTree._innertree.key)
        pass



def init_tree(keys=(2,1,3), items=("v1","v2","v3")):
    bTree = SplayTree()
    for index, val in enumerate(keys):
        bTree[val] = items[index]
    return bTree






