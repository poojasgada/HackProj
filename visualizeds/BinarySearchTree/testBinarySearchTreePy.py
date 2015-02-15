import unittest
from BinarySearchTreePy import *
from StringIO import StringIO
import sys

class BinarySearchTreePyTests(unittest.TestCase):
	def setUp(self):
		return

	def test_searchBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		self.assertEqual(False, testBST.searchBST(testBST.root, 4))
		self.assertEqual(True, testBST.searchBST(testBST.root, 5))
		self.assertEqual(True, testBST.searchBST(testBST.root, 3))
		self.assertEqual(True, testBST.searchBST(testBST.root, 6))
		self.assertEqual(False, testBST.searchBST(testBST.root, 7))

	def test_sizeBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		self.assertEqual(3, testBST.sizeBST(testBST.root))

		testBST.root.left.left = Node(1)

		self.assertEqual(4, testBST.sizeBST(testBST.root))

	def test_printPreorderBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		sys.stdout = StringIO()

		testBST.printPreorderBST(testBST.root)

		# Thank you Stackoverflow for an amazing way to redirect output to a string
		preorder_string  = sys.stdout.getvalue()
		sys.stdout = sys.__stdout__
		self.assertEqual("5 3 6", preorder_string)

	def test_printInorderBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		sys.stdout = StringIO()

		testBST.printInorderBST(testBST.root)

		# Thank you Stackoverflow for an amazing way to redirect output to a string
		inorder_string  = sys.stdout.getvalue()
		sys.stdout = sys.__stdout__
		self.assertEqual("3 5 6", inorder_string)

	def test_printPostorderBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		sys.stdout = StringIO()

		testBST.printPostorderBST(testBST.root)

		# Thank you Stackoverflow for an amazing way to redirect output to a string
		postorder_string  = sys.stdout.getvalue()
		sys.stdout = sys.__stdout__
		self.assertEqual("3 6 5", postorder_string)

	def test_minValBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		self.assertEqual(3, testBST.minValBST(testBST.root))

	def test_maxValBST(self):
		testBST = BST()
		testBST.root = Node(5)
		testBST.root.left = Node(3)
		testBST.root.right = Node(6)

		self.assertEqual(6, testBST.maxValBST(testBST.root))
		

if __name__ == '__main__':
    unittest.main()