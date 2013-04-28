from collections import defaultdict

class Trie():
	"""Trie implementation, some details changed to fit a particular usecase"""
	def __init__(self):
		"""
		Root of the Trie is a dict associating a character to a sub-Trie.
		For the Value, we'll keep 
		"""
		self.root = defaultdict(Trie)
		self.value = None

	
		