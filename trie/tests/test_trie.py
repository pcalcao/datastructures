import unittest
from Trie import Trie
from collections import defaultdict


class TestTrie(unittest.TestCase):

	def test_creation(self):
		trie = Trie()
		self.assertEqual(defaultdict(Trie), trie.root)
		self.assertIsNone(trie.value)
