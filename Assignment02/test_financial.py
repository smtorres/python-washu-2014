import unittest
from financial import *

class FinanceTest(unittest.TestCase):
	
	def setUp(self):
		self.portfolio = Portfolio()

	def test_an_empty_portfolio(self):
		self.assertEqual(0.00, self.portfolio.balance)
		self.assertEqual("Welcome! Empty portfolio \n", self.portfolio.hist)
		self.assertEqual({"Stock" : {}, "Mutual_Fund" : {}}, self.portfolio.items)

	def test_add_cash(self):
		self.portfolio.addCash(300.50)
		self.assertEqual(300.50, self.portfolio.balance)
		self.assertEqual({"Stock" : {}, "Mutual_Fund" : {}}, self.portfolio.items)
		self.assertEqual("Welcome! Empty portfolio \nYou added $ 300.50 in cash, your balance is $ 300.50 \n", self.portfolio.hist)

	def test_stock(self):
		self.s = Stock(20, "HFH")
		self.assertEqual(20, self.s.stock_price)
		self.assertEqual("HFH", self.s.stock_type)

	def test_buy_stock(self):
		self.s = Stock(20, "HFH")
		self.portfolio.addCash(300.50)
		#Test buying an affordable number of stocks
		self.portfolio.buyStock(5, s)
		self.assertEqual(200.50, self.portfolio.balance)
		#Test buying a number of stocks outside the budget
		self.portfolio.buyStock(20, s)
		self.assertEqual({"Stock" : {"HFH" : 5}, "Mutual_Fund" : {}}, self.portfolio.items)
		self.assertEqual(200.50, self.portfolio.balance)
		self.assertEqual({"Stock" : {"HFH" : 5}, "Mutual_Fund" : {}}, self.portfolio.items)

	def test_buy_mf(self):
		self.mf1 = MutualFund("BRT")
		self.mf2 = MutualFund("GHT")
		self.portfolio.addCash(300.50)
		self.portfolio.buyStock(5, s)
		#Buys 10.3 shares of "BRT"
		self.portfolio.buyMutualFund(10.3, self.mf1)
		self.assertEqual(190.20, self.portfolio.balance)
		self.assertEqual({"Stock" : {"HFH" : 5}, "Mutual_Fund" : {"BRT" : 10.3}}, self.portfolio.items)
		#Buys 2 shares of "GHT" but shows error: input not a fraction number
		self.portfolio.buyMutualFund(2, self.mf2)
		self.assertEqual(190.20, self.portfolio.balance)
		self.assertEqual({"Stock" : {"HFH" : 5}, "Mutual_Fund" : {"BRT" : 10.3}}, self.portfolio.items)
		# Buy a new mutual fund
		self.portfolio.buyMutualFund(21.5, self.mf2)
		self.assertEqual(168.70, self.portfolio.balance)
		self.assertEqual({"Stock" : {"HFH" : 5}, "Mutual_Fund" : {"BRT" : 10.3, "GHT": 21.5}}, self.portfolio.items)

	def test_sell_mf(self):
		self.mf1 = MutualFund("BRT")
		self.mf2 = MutualFund("GHT")
		self.portfolio.addCash(300.50)
		self.portfolio.buyMutualFund(10.3, self.mf1)
		#Sells 3 shares of BRT
		self.portfolio.sellMutualFund("BRT", 3)
		self.assertEqual(290.20, self.portfolio.balance)
		self.assertEqual({"Stock" : {}, "Mutual_Fund" : {"BRT" : 10.3}}, self.portfolio.items)

	def test_sell_stock(self):
		self.s = Stock(20, "HFH")
		self.mf1 = MutualFund("BRT")
		self.portfolio.addCash(300.50)
		self.portfolio.buyStock(5, s)
		self.portfolio.buyMutualFund(10.3, self.mf1)
		#Sells 1 share of HFH
		self.portfolio.sellStock("HFH", 1)
		self.assertEqual({"Stock" : {"HFH" : 4}, "Mutual_Fund" : {"BRT" : 10.3}}, self.portfolio.items)
		#Sells 4 share of HFH (Fails, no change)
		self.portfolio.sellStock("HFH", 5)
		self.assertEqual({"Stock" : {"HFH" : 4}, "Mutual_Fund" : {"BRT" : 10.3}}, self.portfolio.items)

	def test_withdraw_cash(self):
		self.portfolio.addCash(300.50)
		self.portfolio.withdrawCash(50)
		self.assertEqual(250.50, self.portfolio.balance)

		
if __name__ == '__main__':
	unittest.main()
	