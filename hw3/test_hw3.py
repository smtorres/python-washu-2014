import unittest
from sort import *
from random import *

class hw3Test(unittest.TestCase):
	def setUp(self):
		self.unsorted1 = [randrange(-1000,1000) for i in xrange(1000)]
		self.unsorted2 = ["1", "765", "-1", "d0", "0", "DgT", "187", "meow"]
		self.sorted1 = sorted(self.unsorted1)
		self.sorted2 = sorted(self.unsorted2)
		
	def test_Bubble(self):
		self.assertEqual(self.sorted1, Bubble(self.unsorted1))
		self.assertEqual(self.sorted2, Bubble(self.unsorted2))
		
	def test_MinSort(self):
		self.assertEqual(self.sorted1, MinSort(self.unsorted1))
		self.assertEqual(self.sorted2, MinSort(self.unsorted2))
			
if __name__ == '__main__':
	unittest.main()