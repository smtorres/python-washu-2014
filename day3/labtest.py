import unittest
import lab3

class MattTest(unittest.TestCase):

	def test_on_shout(self):
		self.assertEqual("HELLO!", lab3.shout("Hello").__str__())
		self.assertEqual("HELLO WORLD!", lab3.shout("HelLo wOrLd").__str__())
		self.assertEqual("HELLO!!", lab3.shout("HELLO!").__str__())
	    
	def test_on_reverse(self):
		self.assertEqual("olleH", lab3.reverse("Hello").__str__())
		self.assertEqual("dLrOw oLleH", lab3.reverse("HelLo wOrLd").__str__())
		self.assertEqual("!OLLEH", lab3.reverse("HELLO!").__str__())
		self.assertEqual("", lab3.reverse(0).__str__())
		
	def test_on_reverse_words(self):
		self.assertEqual("!Hello", lab3.reversewords("Hello!").__str__())
		self.assertEqual("!wOrLd ?HelLo", lab3.reversewords("HelLo? wOrLd!").__str__())
		self.assertEqual("!WORLD HELLO", lab3.reversewords("HELLO WORLD!").__str__()) 
		self.assertEqual(".God my Oh", lab3.reversewords("Oh my God.").__str__())
		
if __name__ == '__main__':
	unittest.main()
	
	