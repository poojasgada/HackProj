'''
LinkedList Library in Python

LinkedList functions supported

- Size of list
- Add a node to end of list
- Add a node to start of list
- Is the list empty
- Searching in a list

'''

class Node:

	def __init__(self, val):
		self.val = val
		self.next = None 

class LinkedList:
	def __init__(self):
		self.listHead = None

	# Check if list is empty
	def isListEmpty(self):
		if not self.listHead:
			return True
		else:
			return False

	# Return the size of the list
	def listSize(self):
		if not self.listHead:
			return 0

		count = 0
		curNode = self.listHead

		while curNode:
			count += 1
			curNode = curNode.next

		return count

	# Just print the list
	def listPrint(self):
		if not self.listHead:
			print "Duh, list is Empty !"
			return

		curNode = self.listHead

		while curNode:
			print curNode.val,
			curNode = curNode.next

		print "\n"
		return

	# Add a node to start or beginning of the list
	def listAddStart(self, newVal):
		if not self.listHead:
			self.listHead = Node(newVal)
			return

		newNode = Node(newVal)
		newNode.next = self.listHead
		self.listHead = newNode
		return

	# Add a node to end of the list
	def listAddEnd(self, newVal):
		if not self.listHead:
			self.listHead = Node(newVal)
			return

		curNode = self.listHead

		while curNode.next:
			curNode = curNode.next

		curNode.next = Node(newVal)
		return

	# Search for a value in the list
	def listSearch(self, searchVal):
		if not self.listHead:
			return False

		curNode = self.listHead

		while curNode:
			if curNode.val == searchVal:
				return True
			curNode = curNode.next

		return False

