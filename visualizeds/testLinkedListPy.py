import unittest
from LinkedListPy import *

class LinkedListPyTests(unittest.TestCase):
	def setUp(self):
		return

	def test_isListEmpty(self):
		testList = LinkedList()
		self.assertEqual(True, testList.isListEmpty())

		testList.listAddEnd(4)
		self.assertEqual(False, testList.isListEmpty())

		# Always nice to cleanup after test
		testList = None

	def test_listSize(self):
		testList = LinkedList()
		self.assertEqual(0, testList.listSize())

		testList.listAddEnd(4)
		testList.listAddEnd(5)
		testList.listAddEnd(7)

		self.assertEqual(3, testList.listSize())

		# Always nice to cleanup after test
		testList = None

	def test_listSearch(self):
		testList = LinkedList()

		testList.listAddEnd(4)
		testList.listAddEnd(5)
		testList.listAddEnd(7)

		self.assertEqual(True, testList.listSearch(4))
		self.assertEqual(False, testList.listSearch(8))

		# Always nice to cleanup after test
		testList = None

	def test_listAddStart(self):
		testList = LinkedList()

		testList.listAddStart(4)
		self.assertEqual(1, testList.listSize())

		testList.listAddStart(5)
		testList.listAddStart(6)
		self.assertEqual(3, testList.listSize())

		# Always nice to cleanup after test
		testList = None

	def test_listAddEnd(self):
		testList = LinkedList()

		testList.listAddEnd(4)
		self.assertEqual(1, testList.listSize())

		testList.listAddEnd(5)
		testList.listAddEnd(6)
		self.assertEqual(3, testList.listSize())

		# Always nice to cleanup after test
		testList = None


if __name__ == '__main__':
    unittest.main()