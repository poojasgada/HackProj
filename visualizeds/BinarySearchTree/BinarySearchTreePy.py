'''
Binary Search Tree Library in Python

Binary Search Tree functions supported

- Search for val
- Print: Preorder, Postorder, Inorder
- Insert
- Delete
- IsBST
- Size

'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None

#BST = Binary Search Tree (Using BST henceforth to preserve my typing sanity)
class BST:
	def __init__(self):
		self.root = None

	# Given a value, search if it is found in the BST
	def searchBST(self, curNode, searchVal):
		if not curNode:
			return False

		if curNode.val == searchVal:
			return True

		if curNode.val < searchVal:
			return self.searchBST(curNode.right, searchVal)
		else:
			return self.searchBST(curNode.left, searchVal)

	# Just print the BST in pre-order traversal
	def printPreorderBST(self, curNode):
		if curNode:
			print curNode.val, 
			self.printPreorderBST(curNode.left)
			self.printPreorderBST(curNode.right)

	# Just print the BST in in-order traversal
	def printInorderBST(self, curNode):
		if curNode:
			self.printInorderBST(curNode.left)
			print curNode.val, 
			self.printInorderBST(curNode.right)

	# Just print the BST in post-order traversal
	def printPostorderBST(self, curNode):
		if curNode:
			self.printPostorderBST(curNode.left)
			self.printPostorderBST(curNode.right)
			print curNode.val, 

	# Get the size of a BST i-e the number of nodes in a BST
	def sizeBST(self, curNode):
		if not curNode:
			return 0
		else:
			return 1 + self.sizeBST(curNode.left) + self.sizeBST(curNode.right)
